"""Kokoro-82M TTS, run directly with onnxruntime (Japanese).

kokoro-onnx is not used because every release requires numpy>=2, which this
project cannot use yet (the Intel-Mac torch build needs numpy<2). The model
only needs phoneme ids, a voice style vector and a speed, so the inference
is a few lines. Japanese text is converted to phonemes by misaki in its
pyopenjtalk mode (no UniDic download needed).
"""

import json
import os

import numpy as np
import onnxruntime as ort
import soundfile as sf
from loguru import logger

from .tts_interface import TTSInterface
from ..asr.utils import download_and_extract

MODEL_URL = (
    "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
)
SAMPLE_RATE = 24000
MAX_TOKENS = 510  # the model's context; voices hold one style per token count

# misaki's pyopenjtalk mode emits a few symbols that are not in Kokoro's
# vocabulary; map them to the IPA the model knows (ʲ = palatalized).
MISAKI_TO_KOKORO = str.maketrans(
    {
        "g": "ɡ",
        "G": "ɡw",
        "K": "kw",
        "ƫ": "tʲ",
        "ᶀ": "bʲ",
        "ᶁ": "dʲ",
        "ᶃ": "ɡʲ",
        "ᶄ": "kʲ",
        "ᶆ": "mʲ",
        "ᶈ": "pʲ",
        "ᶉ": "ɾʲ",
    }
)

with open(
    os.path.join(os.path.dirname(__file__), "kokoro_vocab.json"), encoding="utf-8"
) as f:
    VOCAB: dict[str, int] = json.load(
        f
    )  # from hexgrad/Kokoro-82M config.json (Apache-2.0)


def japanese_to_phonemes(g2p, text: str) -> str:
    # JAG2P returns the phonemes and a same-length pitch string concatenated.
    out, _ = g2p(text)
    return out[: len(out) // 2].translate(MISAKI_TO_KOKORO)


class TTSEngine(TTSInterface):
    def __init__(
        self,
        model_path: str = "models/kokoro/kokoro-v1.0.onnx",
        voices_path: str = "models/kokoro/voices-v1.0.bin",
        voice: str = "jf_alpha",
        speed: float = 1.0,
        lang: str = "ja",
    ):
        """Kokoro TTS.

        Args:
            model_path: Kokoro ONNX model (downloaded on first use if missing).
            voices_path: Kokoro voices file (downloaded on first use if missing).
            voice: Voice name, e.g. jf_alpha, jf_nezumi, jm_kumo.
            speed: Speech speed, 0.5 to 2.0.
            lang: Only 'ja' is supported; use sherpa_onnx_tts for English.
        """
        # ponytail: Japanese only; English would need misaki's heavy spaCy extra.
        if lang != "ja":
            raise ValueError(
                f"kokoro_tts only supports lang 'ja' (got '{lang}'). "
                "Use sherpa_onnx_tts for English."
            )
        for path in (model_path, voices_path):
            if not os.path.exists(path):
                logger.warning(f"Kokoro file not found, downloading: {path}")
                download_and_extract(
                    MODEL_URL + os.path.basename(path), os.path.dirname(path)
                )

        from misaki import ja  # imported here: loading the dictionary takes ~2 s

        self.g2p = ja.JAG2P(version="pyopenjtalk")
        self.session = ort.InferenceSession(model_path)
        voices = np.load(voices_path)
        if voice not in voices.files:
            raise ValueError(
                f"Unknown Kokoro voice '{voice}'. Available: {voices.files}"
            )
        self.style = voices[voice]  # (MAX_TOKENS, 1, 256)
        self.speed = speed
        self.file_extension = "wav"

    def generate_audio(self, text: str, file_name_no_ext=None) -> str | None:
        file_name = self.generate_cache_file_name(file_name_no_ext, self.file_extension)
        try:
            phonemes = japanese_to_phonemes(self.g2p, text)
            tokens = [VOCAB[p] for p in phonemes if p in VOCAB][: MAX_TOKENS - 2]
            if not tokens:
                return None
            audio = self.session.run(
                None,
                {
                    "tokens": np.array([[0, *tokens, 0]], dtype=np.int64),
                    "style": self.style[len(tokens)].astype(np.float32),
                    "speed": np.array([self.speed], dtype=np.float32),
                },
            )[0]
            sf.write(
                file_name, np.asarray(audio).ravel(), SAMPLE_RATE, subtype="PCM_16"
            )
            return file_name
        except Exception as e:
            logger.error(f"Kokoro TTS unable to generate audio: {e}")
            return None
