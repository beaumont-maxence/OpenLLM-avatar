from loguru import logger

from .tts_interface import TTSInterface


class FallbackTTS(TTSInterface):
    """Use the primary engine, and the fallback engine when the primary fails
    (for example, the GPT-SoVITS server is not running)."""

    def __init__(self, primary: TTSInterface | None, fallback: TTSInterface):
        self.primary = primary
        self.fallback = fallback
        self._warned = False

    def generate_audio(self, text: str, file_name_no_ext=None) -> str | None:
        if self.primary is not None:
            try:
                path = self.primary.generate_audio(text, file_name_no_ext)
                if path:
                    return path
            except Exception as e:
                # Warn once; a stopped server would otherwise log on every sentence.
                log = logger.debug if self._warned else logger.warning
                log(f"Primary TTS failed ({e}); using the fallback voice.")
                self._warned = True
        return self.fallback.generate_audio(text, file_name_no_ext)
