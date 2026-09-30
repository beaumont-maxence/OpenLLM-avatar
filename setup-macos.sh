#!/usr/bin/env bash
# One-time setup for OpenLLM-avatar on macOS. Safe to re-run.
#   ./setup-macos.sh
# Installs uv and Ollama (via Homebrew) if missing, installs Python dependencies,
# creates conf.yaml, pulls the Ollama model, and downloads the speech models.
set -euo pipefail
cd "$(dirname "$0")"

step() { printf '\n==> %s\n' "$1"; }
fail() { printf 'Error: %s\n' "$1" >&2; exit 1; }

[[ "$(uname -s)" == "Darwin" ]] || fail "this script is for macOS."
arch="$(uname -m)"

# A fresh Homebrew install is not on PATH until the shell profile is reloaded.
if ! command -v brew >/dev/null; then
  for b in /opt/homebrew/bin/brew /usr/local/bin/brew; do
    if [[ -x "$b" ]]; then eval "$("$b" shellenv)"; break; fi
  done
fi
# Ollama.app downloaded from ollama.com only links its CLI after the first launch.
if ! command -v ollama >/dev/null && [[ -x /Applications/Ollama.app/Contents/Resources/ollama ]]; then
  PATH="$PATH:/Applications/Ollama.app/Contents/Resources"
fi

brew_install() { # brew_install <command> <brew args...>
  command -v "$1" >/dev/null && return
  command -v brew >/dev/null ||
    fail "$1 is missing. Install Homebrew (https://brew.sh) or $1 yourself, then re-run."
  step "Installing $1 with Homebrew"
  brew install "${@:2}"
}

brew_install uv uv
brew_install ollama --cask ollama-app

step "Installing Python dependencies (first run downloads ~1 GB)"
uv sync --locked

if [[ ! -f conf.yaml ]]; then
  step "Creating conf.yaml from config_templates/conf.macos.yaml"
  cp config_templates/conf.macos.yaml conf.yaml
  if [[ "$arch" == "x86_64" ]]; then # MLX models only run on Apple Silicon
    sed -i '' "s/model: 'qwen3.5:9b-mlx'.*/model: 'qwen3.5:9b'/" conf.yaml
  fi
else
  step "Keeping existing conf.yaml"
fi

# Prints the Ollama model if conf.yaml uses Ollama, nothing otherwise.
model="$(uv run --no-sync python - <<'EOF'
from src.open_llm_vtuber.config_manager.utils import read_yaml, validate_config
agent = validate_config(read_yaml("conf.yaml")).character_config.agent_config
if agent.agent_settings.basic_memory_agent.llm_provider == "ollama_llm":
    print(agent.llm_configs.ollama_llm.model)
EOF
)"

if [[ -n "$model" ]]; then
  if ! curl -sf http://localhost:11434/api/version >/dev/null; then
    step "Starting Ollama"
    open -a Ollama 2>/dev/null || (ollama serve >/dev/null 2>&1 &)
    for _ in $(seq 30); do
      curl -sf http://localhost:11434/api/version >/dev/null && break
      sleep 1
    done
    curl -sf http://localhost:11434/api/version >/dev/null || fail "Ollama did not start."
  fi
  if ollama show "$model" >/dev/null 2>&1; then
    step "Ollama model $model is already installed"
  else
    step "Pulling Ollama model $model"
    ollama pull "$model"
  fi
fi

step "Downloading speech models (skipped if already present)"
uv run --no-sync python - <<'EOF'
from src.open_llm_vtuber.config_manager.utils import read_yaml, validate_config
from src.open_llm_vtuber.asr.asr_factory import ASRFactory
from src.open_llm_vtuber.tts.tts_factory import TTSFactory

character = validate_config(read_yaml("conf.yaml")).character_config
asr, tts = character.asr_config, character.tts_config
ASRFactory.get_asr_system(asr.asr_model, **getattr(asr, asr.asr_model).model_dump())
TTSFactory.get_tts_engine(tts.tts_model, **getattr(tts, tts.tts_model).model_dump())
TTSFactory.get_tts_engine("kokoro_tts")  # Japanese fallback voice of "Yui (日本語)"
EOF

cat <<'EOF'

Setup complete. Start the assistant with:
    uv run run_server.py
then open http://localhost:12393 in your browser.

Camera and microphone: allow your browser in
System Settings > Privacy & Security > Camera / Microphone, then restart it.
EOF
