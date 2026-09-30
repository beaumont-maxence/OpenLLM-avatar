import sys

import pytest

from src.open_llm_vtuber.config_manager.utils import read_yaml, validate_config

CLOUD_MODULES = [
    "anthropic",
    "azure",
    "cartesia",
    "edge_tts",
    "elevenlabs",
    "groq",
    "letta_client",
]


@pytest.mark.parametrize(
    "path",
    ["config_templates/conf.macos.yaml", "config_templates/conf.windows-nvidia.yaml"],
)
def test_local_templates_are_valid(path):
    config = validate_config(read_yaml(path))
    assert (
        config.character_config.agent_config.agent_settings.basic_memory_agent.llm_provider
        == "ollama_llm"
    )


def test_server_imports_without_cloud_sdks():
    import src.open_llm_vtuber.server  # noqa: F401
    import src.open_llm_vtuber.service_context  # noqa: F401

    assert [m for m in CLOUD_MODULES if m in sys.modules] == []
