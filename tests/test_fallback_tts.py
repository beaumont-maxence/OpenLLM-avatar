from src.open_llm_vtuber.tts.fallback_tts import FallbackTTS
from src.open_llm_vtuber.tts.tts_interface import TTSInterface


class Fixed(TTSInterface):
    def __init__(self, result):
        self.result = result

    def generate_audio(self, text, file_name_no_ext=None):
        if isinstance(self.result, Exception):
            raise self.result
        return self.result


def test_uses_primary_when_it_works():
    assert FallbackTTS(Fixed("a.wav"), Fixed("b.wav")).generate_audio("hi") == "a.wav"


def test_falls_back_when_primary_raises_or_returns_nothing():
    assert (
        FallbackTTS(Fixed(ConnectionError()), Fixed("b.wav")).generate_audio("hi")
        == "b.wav"
    )
    assert FallbackTTS(Fixed(None), Fixed("b.wav")).generate_audio("hi") == "b.wav"
    assert FallbackTTS(None, Fixed("b.wav")).generate_audio("hi") == "b.wav"
