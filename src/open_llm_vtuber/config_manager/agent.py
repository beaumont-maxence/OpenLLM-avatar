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
        "llama_cpp_llm",
        "ollama_llm",
        "lmstudio_llm",
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


# =================================


class AgentSettings(I18nMixin, BaseModel):
    """Settings for different types of agents."""

    basic_memory_agent: Optional[BasicMemoryAgentConfig] = Field(
        None, alias="basic_memory_agent"
    )

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "basic_memory_agent": Description(
            en="Configuration for basic memory agent",
            ja="ベーシックメモリエージェントの設定",
        ),
    }


class AgentConfig(I18nMixin, BaseModel):
    """This class contains all of the configurations related to agent."""

    conversation_agent_choice: Literal["basic_memory_agent"] = Field(
        ..., alias="conversation_agent_choice"
    )
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
