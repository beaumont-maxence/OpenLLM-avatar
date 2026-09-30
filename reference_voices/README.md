# Reference Voices

Reference audio clips for zero-shot voice cloning via GPT-SoVITS.
Only clone voices you own or have explicit permission to use.

## Yui's Japanese voice

`characters/yui_ja.yaml` clones `reference_voices/testvoice.wav`. To use another clip,
change `ref_audio_path` there (relative paths are from the project root), and put the
clip's exact transcript in `prompt_text`. Leaving `prompt_text` empty works but sounds
less like the clip.

## Adding a voice

1. Record or obtain a **clean 3–10 second WAV** of the target voice
   (one speaker, no background music/noise).
2. Register it:

   ```sh
   uv run add_voice.py my_voice.wav "exact transcript of what is said" --lang ja
   ```

   This copies the WAV here and creates `characters/voice_<name>.yaml`.
3. Start the GPT-SoVITS server (below), then `uv run run_server.py` and
   pick **Voice: \<name\>** in the web UI character dropdown. Switching
   characters hot-swaps the TTS voice — no restart needed.

## One-time GPT-SoVITS server setup

Cloning is performed by a separate GPT-SoVITS server that this app calls
at `http://127.0.0.1:9880/tts`:

```sh
git clone https://github.com/RVC-Boss/GPT-SoVITS
cd GPT-SoVITS
# follow its install docs (macOS: conda env, `bash install.sh`)
python api_v2.py   # serves http://127.0.0.1:9880
```

Notes:
- `add_voice.py` writes an **absolute** `ref_audio_path`, so the server
  (a separate process with its own working directory) can find the clip.
  Keep this folder in place, or re-run `add_voice.py` after moving it.
- Supported `--lang` values here: `ja`, `zh`, `en`.
- To use a different endpoint, pass `--api-url`.
