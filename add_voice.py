"""Create a cloned-voice character config from a reference WAV.

Copies the WAV into reference_voices/ and writes a character YAML that
overrides tts_config to use GPT-SoVITS zero-shot cloning. The new voice
appears in the web UI character dropdown; switching to it hot-swaps TTS.

Usage:
    uv run add_voice.py my_voice.wav "transcript of the clip" --lang ja
"""

import argparse
import shutil
import sys
from pathlib import Path

import soundfile as sf
import yaml

REFERENCE_DIR = Path("reference_voices")
CHARACTERS_DIR = Path("characters")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Register a reference voice for GPT-SoVITS cloning."
    )
    parser.add_argument("wav_path", help="Reference audio clip (3-10s WAV)")
    parser.add_argument("transcript", help="Exact transcript of the clip")
    parser.add_argument("--name", help="Voice name (default: wav filename stem)")
    parser.add_argument(
        "--lang",
        default="ja",
        choices=["ja", "zh", "en"],
        help="Language of the clip and of generated speech (default: ja)",
    )
    parser.add_argument(
        "--api-url",
        default="http://127.0.0.1:9880/tts",
        help="GPT-SoVITS API endpoint",
    )
    parser.add_argument(
        "--force", action="store_true", help="Overwrite an existing voice config"
    )
    args = parser.parse_args()

    wav_path = Path(args.wav_path)
    if not wav_path.is_file():
        print(f"Error: file not found: {wav_path}")
        return 1

    try:
        duration = sf.info(wav_path).duration
    except Exception as e:
        print(f"Error: cannot read audio file ({e})")
        return 1
    if not 3.0 <= duration <= 10.0:
        print(
            f"Warning: clip is {duration:.1f}s; GPT-SoVITS works best with "
            "3-10s references and may reject clips outside that range."
        )

    name = args.name or wav_path.stem
    config_path = CHARACTERS_DIR / f"voice_{name}.yaml"
    if config_path.exists() and not args.force:
        print(f"Error: {config_path} already exists. Use --force to overwrite.")
        return 1

    REFERENCE_DIR.mkdir(exist_ok=True)
    ref_path = (REFERENCE_DIR / f"{name}.wav").resolve()
    if wav_path.resolve() != ref_path:
        shutil.copy(wav_path, ref_path)

    config = {
        "character_config": {
            "conf_name": f"Voice: {name}",
            "conf_uid": f"voice_{name}",
            "tts_config": {
                "tts_model": "gpt_sovits_tts",
                "gpt_sovits_tts": {
                    "api_url": args.api_url,
                    # ponytail: absolute path so the GPT-SoVITS server
                    # (separate process, own cwd) can resolve it
                    "ref_audio_path": str(ref_path),
                    "prompt_text": args.transcript,
                    "prompt_lang": args.lang,
                    "text_lang": args.lang,
                    "text_split_method": "cut5",
                    "batch_size": "1",
                    "media_type": "wav",
                    "streaming_mode": "false",
                },
            },
        }
    }
    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)

    print(f"Saved reference audio: {ref_path}")
    print(f"Created character config: {config_path}")
    print("\nNext steps:")
    print("  1. Start the GPT-SoVITS server (see reference_voices/README.md)")
    print("  2. uv run run_server.py")
    print(f"  3. Pick 'Voice: {name}' in the web UI character dropdown")
    return 0


if __name__ == "__main__":
    sys.exit(main())
