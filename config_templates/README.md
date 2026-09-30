# Config Templates

Copy one of these to the project root as `conf.yaml` (on first start, `run_server.py`
copies `conf.macos.yaml` on macOS and `conf.default.yaml` elsewhere):

- `conf.macos.yaml`: macOS, fully local (also works as a CPU-only config on Windows).
- `conf.windows-nvidia.yaml`: Windows with an NVIDIA GPU (`uv sync --extra nvidia`).
- `conf.default.yaml`, `conf.ZH.default.yaml`, `conf.JP.default.yaml`: generic local
  configs with English, Chinese and Japanese comments.
