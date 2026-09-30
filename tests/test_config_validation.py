import pytest
from pydantic import ValidationError

from src.open_llm_vtuber.config_manager.asr import ASRConfig, FasterWhisperConfig
from src.open_llm_vtuber.config_manager.tts import BarkTTSConfig, TTSConfig
from src.open_llm_vtuber.config_manager.utils import read_yaml, validate_config


def test_tts_config_requires_selected_model_block():
    with pytest.raises(ValidationError, match="bark_tts"):
        TTSConfig(tts_model="bark_tts")


def test_tts_config_accepts_selected_model_with_block():
    config = TTSConfig(
        tts_model="bark_tts",
        bark_tts=BarkTTSConfig(voice="v2/en_speaker_1"),
    )
    assert config.tts_model == "bark_tts"


def test_asr_config_requires_selected_model_block():
    with pytest.raises(ValidationError, match="faster_whisper"):
        ASRConfig(asr_model="faster_whisper")


def test_asr_config_accepts_selected_model_with_block():
    config = ASRConfig(
        asr_model="faster_whisper",
        faster_whisper=FasterWhisperConfig(
            model_path="distil-medium.en", download_root="models"
        ),
    )
    assert config.asr_model == "faster_whisper"


@pytest.mark.parametrize(
    "template",
    [
        "config_templates/conf.default.yaml",
        "config_templates/conf.ZH.default.yaml",
    ],
)
def test_default_templates_validate(template):
    validate_config(read_yaml(template))
