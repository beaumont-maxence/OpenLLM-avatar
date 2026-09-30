# config_manager/system.py
from pydantic import Field, model_validator
from typing import Dict, ClassVar
from .i18n import I18nMixin, Description


class SystemConfig(I18nMixin):
    """System configuration settings."""

    host: str = Field(..., alias="host")
    port: int = Field(..., alias="port")
    config_alts_dir: str = Field(..., alias="config_alts_dir")
    tool_prompts: Dict[str, str] = Field(..., alias="tool_prompts")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "host": Description(en="Server host address", ja="サーバーのホストアドレス"),
        "port": Description(en="Server port number", ja="サーバーのポート番号"),
        "config_alts_dir": Description(
            en="Directory for alternative configurations",
            ja="代替設定用ディレクトリ",
        ),
        "tool_prompts": Description(
            en="Tool prompts to be inserted into persona prompt",
            ja="ペルソナプロンプトに挿入するツールプロンプト",
        ),
    }

    @model_validator(mode="after")
    def check_port(cls, values):
        port = values.port
        if port < 0 or port > 65535:
            raise ValueError("Port must be between 0 and 65535")
        return values
