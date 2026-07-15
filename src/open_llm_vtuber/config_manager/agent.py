"""
This module contains the pydantic model for the configurations of
different types of agents.
"""

from pydantic import BaseModel, Field
from typing import Dict, ClassVar, Optional, Literal, List
from .i18n import I18nMixin, Description
from .stateless_llm import StatelessLLMConfigs

# ======== Configurations for different Agents ========


class BasicMemoryAgentConfig(I18nMixin, BaseModel):
    """Configuration for the basic memory agent."""

    llm_provider: Literal[
        "stateless_llm_with_template",
        "openai_compatible_llm",
        "claude_llm",
        "llama_cpp_llm",
        "ollama_llm",
        "lmstudio_llm",
        "openai_llm",
        "gemini_llm",
        "zhipu_llm",
        "deepseek_llm",
        "groq_llm",
        "mistral_llm",
    ] = Field(..., alias="llm_provider")

    faster_first_response: Optional[bool] = Field(True, alias="faster_first_response")
    segment_method: Literal["regex", "pysbd"] = Field("pysbd", alias="segment_method")
    use_mcpp: Optional[bool] = Field(False, alias="use_mcpp")
    mcp_enabled_servers: Optional[List[str]] = Field([], alias="mcp_enabled_servers")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "llm_provider": Description(
            en="LLM provider to use for this agent",
            ja="このエージェントが使用するLLMプロバイダー",
        ),
        "faster_first_response": Description(
            en="Whether to respond as soon as encountering a comma in the first sentence to reduce latency (default: True)",
            ja="最初の文でカンマに遭遇した時点で応答を開始し、遅延を減らすかどうか（デフォルト: True）",
        ),
        "segment_method": Description(
            en="Method for segmenting sentences: 'regex' or 'pysbd' (default: 'pysbd')",
            ja="文を分割する方法：'regex' または 'pysbd'（デフォルト: 'pysbd'）",
        ),
        "use_mcpp": Description(
            en="Whether to use MCP (Model Context Protocol) for the agent (default: True)",
            ja="エージェントでMCP（Model Context Protocol）を使用するかどうか（デフォルト: True）",
        ),
        "mcp_enabled_servers": Description(
            en="List of MCP servers to enable for the agent",
            ja="エージェントで有効にするMCPサーバーのリスト",
        ),
    }


class HumeAIConfig(I18nMixin, BaseModel):
    """Configuration for the Hume AI agent."""

    api_key: str = Field(..., alias="api_key")
    host: str = Field("api.hume.ai", alias="host")
    config_id: Optional[str] = Field(None, alias="config_id")
    idle_timeout: int = Field(15, alias="idle_timeout")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "api_key": Description(
            en="API key for Hume AI service",
            ja="Hume AIサービスのAPIキー",
        ),
        "host": Description(
            en="Host URL for Hume AI service (default: api.hume.ai)",
            ja="Hume AIサービスのホストURL（デフォルト: api.hume.ai）",
        ),
        "config_id": Description(
            en="Configuration ID for EVI settings",
            ja="EVI設定の構成ID",
        ),
        "idle_timeout": Description(
            en="Idle timeout in seconds before disconnecting (default: 15)",
            ja="切断までのアイドルタイムアウト秒数（デフォルト: 15）",
        ),
    }


# =================================


class LettaConfig(I18nMixin, BaseModel):
    """Configuration for the Letta agent."""

    host: str = Field("localhost", alias="host")
    port: int = Field(8283, alias="port")
    id: str = Field(..., alias="id")
    faster_first_response: Optional[bool] = Field(True, alias="faster_first_response")
    segment_method: Literal["regex", "pysbd"] = Field("pysbd", alias="segment_method")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "host": Description(
            en="Host address for the Letta server",
            ja="Lettaサーバーのホストアドレス",
        ),
        "port": Description(
            en="Port number for the Letta server (default: 8283)",
            ja="Lettaサーバーのポート番号（デフォルト: 8283）",
        ),
        "id": Description(
            en="Agent instance ID running on the Letta server",
            ja="Lettaサーバー上で実行されているエージェントインスタンスのID",
        ),
    }


class AgentSettings(I18nMixin, BaseModel):
    """Settings for different types of agents."""

    basic_memory_agent: Optional[BasicMemoryAgentConfig] = Field(
        None, alias="basic_memory_agent"
    )
    hume_ai_agent: Optional[HumeAIConfig] = Field(None, alias="hume_ai_agent")
    letta_agent: Optional[LettaConfig] = Field(None, alias="letta_agent")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "basic_memory_agent": Description(
            en="Configuration for basic memory agent",
            ja="ベーシックメモリエージェントの設定",
        ),
        "hume_ai_agent": Description(
            en="Configuration for Hume AI agent",
            ja="Hume AIエージェントの設定",
        ),
        "letta_agent": Description(
            en="Configuration for Letta agent",
            ja="Lettaエージェントの設定",
        ),
    }


class AgentConfig(I18nMixin, BaseModel):
    """This class contains all of the configurations related to agent."""

    conversation_agent_choice: Literal[
        "basic_memory_agent", "hume_ai_agent", "letta_agent"
    ] = Field(..., alias="conversation_agent_choice")
    agent_settings: AgentSettings = Field(..., alias="agent_settings")
    llm_configs: StatelessLLMConfigs = Field(..., alias="llm_configs")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "conversation_agent_choice": Description(
            en="Type of conversation agent to use",
            ja="使用する会話エージェントの種類",
        ),
        "agent_settings": Description(
            en="Settings for different agent types",
            ja="各エージェントタイプの設定",
        ),
        "llm_configs": Description(
            en="Pool of LLM provider configurations",
            ja="LLMプロバイダー設定のプール",
        ),
        "faster_first_response": Description(
            en="Whether to respond as soon as encountering a comma in the first sentence to reduce latency (default: True)",
            ja="最初の文でカンマに遭遇した時点で応答を開始し、遅延を減らすかどうか（デフォルト: True）",
        ),
        "segment_method": Description(
            en="Method for segmenting sentences: 'regex' or 'pysbd' (default: 'pysbd')",
            ja="文を分割する方法：'regex' または 'pysbd'（デフォルト: 'pysbd'）",
        ),
    }
