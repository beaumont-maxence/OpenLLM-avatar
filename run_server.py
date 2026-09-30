import os
import sys
import atexit
import asyncio
import argparse
import shutil
from pathlib import Path
import tomli
import uvicorn
from loguru import logger

from src.open_llm_vtuber.server import WebSocketServer
from src.open_llm_vtuber.config_manager import Config, read_yaml, validate_config

os.environ["HF_HOME"] = str(Path(__file__).parent / "models")
os.environ["MODELSCOPE_CACHE"] = str(Path(__file__).parent / "models")


def get_version() -> str:
    with open("pyproject.toml", "rb") as f:
        pyproject = tomli.load(f)
    return pyproject["project"]["version"]


def init_logger(console_log_level: str = "INFO") -> None:
    logger.remove()
    # Console output
    logger.add(
        sys.stderr,
        level=console_log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | {message}",
        colorize=True,
    )

    # File output
    logger.add(
        "logs/debug_{time:YYYY-MM-DD}.log",
        rotation="10 MB",
        retention="30 days",
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} | {message} | {extra}",
        backtrace=True,
        diagnose=True,
    )


def check_frontend():
    """Log an error if the prebuilt web UI in frontend/ is missing.

    Upstream ships frontend/ as a git submodule; this repo tracks the built files
    directly, so the fix is to restore them from git.
    """
    if not (Path(__file__).parent / "frontend" / "index.html").exists():
        logger.critical(
            'frontend/index.html is missing, so the browser will show {"detail":"Not Found"}.\n'
            "Restore the tracked web UI files with: git restore frontend"
        )


def parse_args():
    parser = argparse.ArgumentParser(description="OpenLLM-avatar server")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    return parser.parse_args()


def ensure_user_config() -> None:
    """Create conf.yaml from the platform's local template on first start."""
    if Path("conf.yaml").exists():
        return
    template = "conf.macos.yaml" if sys.platform == "darwin" else "conf.default.yaml"
    shutil.copy2(Path("config_templates") / template, "conf.yaml")
    logger.warning(f"conf.yaml not found: created it from config_templates/{template}")


@logger.catch
def run(console_log_level: str):
    init_logger(console_log_level)
    logger.info(f"OpenLLM-avatar, version v{get_version()}")

    check_frontend()
    ensure_user_config()

    atexit.register(WebSocketServer.clean_cache)

    # Load configurations from yaml file
    config: Config = validate_config(read_yaml("conf.yaml"))
    server_config = config.system_config

    # Initialize the WebSocket server (synchronous part)
    server = WebSocketServer(config=config)

    # Perform asynchronous initialization (loading context, etc.)
    logger.info("Initializing server context...")
    try:
        asyncio.run(server.initialize())
        logger.info("Server context initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize server context: {e}")
        sys.exit(1)  # Exit if initialization fails

    # Run the Uvicorn server
    logger.info(f"Starting server on {server_config.host}:{server_config.port}")
    uvicorn.run(
        app=server.app,
        host=server_config.host,
        port=server_config.port,
        log_level=console_log_level.lower(),
    )


if __name__ == "__main__":
    args = parse_args()
    console_log_level = "DEBUG" if args.verbose else "INFO"
    if args.verbose:
        logger.info("Running in verbose mode")
    else:
        logger.info(
            "Running in standard mode. For detailed debug logs, use: uv run run_server.py --verbose"
        )
    run(console_log_level=console_log_level)
