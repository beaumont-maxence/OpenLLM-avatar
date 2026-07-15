import os

import soundfile as sf
from loguru import logger

from .tts_interface import TTSInterface

try:
    from kokoro_onnx import Kokoro

    KOKORO_AVAILABLE = True
except ImportError:
    KOKORO_AVAILABLE = False
    logger.warning("kokoro-onnx not installed. Run: uv add kokoro-onnx")


# Kokoro TTS requires the ONNX model and voices files:
# Download kokoro-v1.0.onnx (~310 MB) and voices-v1.0.bin from:
# https://github.com/thewh1teagle/kokoro-onnx/releases
# Place both files in the models/kokoro/ directory.
# Voice examples: af_sarah, af_heart, am_adam (English),
# jf_alpha, jm_kumo (Japanese), zf_xiaobei (Chinese)
# Language codes: en-us, en-gb, ja, cmn, fr-fr, ...


class TTSEngine(TTSInterface):
    def __init__(
        self,
        model_path: str = "models/kokoro/kokoro-v1.0.onnx",
        voices_path: str = "models/kokoro/voices-v1.0.bin",
        voice: str = "af_sarah",
        speed: float = 1.0,
        lang: str = "en-us",
    ):
        """Initializes the Kokoro TTS engine using kokoro-onnx.

        Args:
            model_path: Path to the Kokoro ONNX model file.
            voices_path: Path to the Kokoro voices file.
            voice: Voice name (e.g., af_sarah, jf_alpha).
            speed: Speech speed (1.0 is normal).
            lang: Language code (e.g., en-us, ja).
        """
        if not KOKORO_AVAILABLE:
            raise ImportError(
                "kokoro-onnx is required. Install with: uv add kokoro-onnx"
            )

        self.voice = voice
        self.speed = speed
        self.lang = lang
        self.file_extension = "wav"

        for path in (model_path, voices_path):
            if not os.path.exists(path):
                logger.warning(f"Kokoro model file not found at: {path}")
                logger.warning(
                    "Download kokoro-v1.0.onnx and voices-v1.0.bin from: "
                    "https://github.com/thewh1teagle/kokoro-onnx/releases"
                )
                raise FileNotFoundError(f"Model file not found: {path}")

        try:
            logger.info(f"Loading Kokoro model: {model_path}")
            self.kokoro = Kokoro(model_path, voices_path)
            logger.info("Kokoro model loaded successfully")
        except Exception as e:
            logger.critical(f"Failed to load Kokoro model: {e}")
            raise

    def generate_audio(
        self, text: str, file_name_no_ext: str | None = None
    ) -> str | None:
        """Generates a speech audio file using Kokoro TTS.

        Args:
            text: The text to convert to speech.
            file_name_no_ext: The name of the file without the extension. Defaults to None.

        Returns:
            The path to the generated audio file, or None on failure.
        """
        file_name = self.generate_cache_file_name(file_name_no_ext, self.file_extension)

        try:
            samples, sample_rate = self.kokoro.create(
                text, voice=self.voice, speed=self.speed, lang=self.lang
            )
            sf.write(file_name, samples, sample_rate, subtype="PCM_16")
            logger.info(f"Generated audio file: {file_name}")
            return file_name

        except Exception as e:
            logger.critical(f"Error: Kokoro TTS unable to generate audio: {e}")
            return None
