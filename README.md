<h1 align="center">OpenLLM-avatar</h1>

A local, privacy-friendly AI companion: webcam and microphone in, local models
(speech recognition, an LLM via Ollama, text-to-speech), and an animated Live2D
avatar out. Everything can run offline. It is the first step toward a physical
android, so ASR, LLM, TTS, vision and the avatar stay swappable modules.

Based on [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber)
v1.2.1 (see [Credits](#credits)).

## Install

Requirements: [uv](https://docs.astral.sh/uv/getting-started/installation/),
[Ollama](https://ollama.com/download), git, and a Chromium-based browser or Firefox.
The first start downloads the speech models (~1 GB) into `models/`. After that, no
internet connection is needed.

### macOS (Apple Silicon; Intel should work)

```sh
git clone https://github.com/beaumont-maxence/OpenLLM-avatar.git
cd OpenLLM-avatar
./setup-macos.sh
uv run run_server.py
```

`setup-macos.sh` installs uv and Ollama with Homebrew if they're missing, installs the
Python dependencies, creates `conf.yaml`, pulls the Ollama model (`qwen3.5:9b` on
Intel Macs) and downloads the speech models. It is safe to re-run.

### Windows with an NVIDIA GPU

```powershell
git clone https://github.com/beaumont-maxence/OpenLLM-avatar.git
cd OpenLLM-avatar
uv sync --extra nvidia
copy config_templates\conf.windows-nvidia.yaml conf.yaml
ollama pull qwen3.5:9b
uv run run_server.py
```

This installs PyTorch with CUDA 12.8 and uses faster-whisper on the GPU for speech
recognition. Keep your NVIDIA driver up to date.

### Windows without an NVIDIA GPU

Same as above, but run `uv sync` (no extra) and copy `conf.macos.yaml`. It is a
CPU-only config that works on any OS. Then set the Ollama model in `conf.yaml` to
`qwen3.5:9b`.

Open http://localhost:12393 in your browser once the server says it's running.

Only local engines are included; the upstream cloud providers (Claude, OpenAI,
Azure, ElevenLabs, Edge TTS, and others) were removed, so no API keys are needed.

## Camera and microphone permissions

- The browser only allows the camera and microphone on **localhost or HTTPS**. To
  use the app from another device, put it behind an HTTPS reverse proxy.
- **macOS:** grant access to your browser under **System Settings → Privacy &
  Security → Camera / Microphone**, then restart the browser.
- **Windows:** check **Settings → Privacy & security → Camera / Microphone** and
  make sure "Let desktop apps access…" is on.

When the camera is on, the web UI sends one frame with each message you send. The
LLM has to be a vision model (the defaults above are) to use it.

## Credits

This project is a copy of
[Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) by the
Open-LLM-VTuber contributors, used under the MIT License (see [LICENSE](./LICENSE)).
The web frontend in `frontend/` is the prebuilt
[Open-LLM-VTuber-Web](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber-Web) UI.
Upstream's documentation at https://open-llm-vtuber.github.io/docs/ still applies to
most configuration options.

## Third-Party Licenses

### Live2D Sample Models Notice

This project includes Live2D sample models provided by Live2D Inc. These assets are licensed separately under the Live2D Free Material License Agreement and the Terms of Use for Live2D Cubism Sample Data. They are not covered by the MIT license of this project.

This content uses sample data owned and copyrighted by Live2D Inc. The sample data are utilized in accordance with the terms and conditions set by Live2D Inc. (See [Live2D Free Material License Agreement](https://www.live2d.jp/en/terms/live2d-free-material-license-agreement/) and [Terms of Use](https://www.live2d.com/eula/live2d-sample-model-terms_en.html)).

Note: For commercial use, especially by medium or large-scale enterprises, the use of these Live2D sample models may be subject to additional licensing requirements. If you plan to use this project commercially, please ensure that you have the appropriate permissions from Live2D Inc., or use versions of the project without these models.

The full Live2D license text is in [LICENSE-Live2D.md](./LICENSE-Live2D.md).
