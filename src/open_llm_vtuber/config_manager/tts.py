# config_manager/tts.py
from pydantic import ValidationInfo, Field, model_validator
from typing import Literal, Optional, Dict, ClassVar
from .i18n import I18nMixin, Description


class BarkTTSConfig(I18nMixin):
    """Configuration for Bark TTS."""

    voice: str = Field(..., alias="voice")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "voice": Description(
            en="Voice name to use for Bark TTS",
            ja="Bark TTSで使用する音声名",
        ),
    }


class CosyvoiceTTSConfig(I18nMixin):
    """Configuration for Cosyvoice TTS."""

    client_url: str = Field(..., alias="client_url")
    mode_checkbox_group: str = Field(..., alias="mode_checkbox_group")
    sft_dropdown: str = Field(..., alias="sft_dropdown")
    prompt_text: str = Field(..., alias="prompt_text")
    prompt_wav_upload_url: str = Field(..., alias="prompt_wav_upload_url")
    prompt_wav_record_url: str = Field(..., alias="prompt_wav_record_url")
    instruct_text: str = Field(..., alias="instruct_text")
    seed: int = Field(..., alias="seed")
    api_name: str = Field(..., alias="api_name")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "client_url": Description(
            en="URL of the CosyVoice Gradio web UI",
            ja="CosyVoice Gradio WebUIのURL",
        ),
        "mode_checkbox_group": Description(
            en="Mode checkbox group value",
            ja="モードチェックボックスグループの値",
        ),
        "sft_dropdown": Description(
            en="SFT dropdown value", ja="SFTドロップダウンの値"
        ),
        "prompt_text": Description(en="Prompt text", ja="プロンプトテキスト"),
        "prompt_wav_upload_url": Description(
            en="URL for prompt WAV file upload",
            ja="プロンプトWAVファイルのアップロード先URL",
        ),
        "prompt_wav_record_url": Description(
            en="URL for prompt WAV file recording",
            ja="プロンプトWAVファイルの録音先URL",
        ),
        "instruct_text": Description(en="Instruction text", ja="指示テキスト"),
        "seed": Description(en="Random seed", ja="乱数シード"),
        "api_name": Description(en="API endpoint name", ja="APIエンドポイント名"),
    }


class Cosyvoice2TTSConfig(I18nMixin):
    """Configuration for Cosyvoice2 TTS."""

    client_url: str = Field(..., alias="client_url")
    mode_checkbox_group: str = Field(..., alias="mode_checkbox_group")
    sft_dropdown: str = Field(..., alias="sft_dropdown")
    prompt_text: str = Field(..., alias="prompt_text")
    prompt_wav_upload_url: str = Field(..., alias="prompt_wav_upload_url")
    prompt_wav_record_url: str = Field(..., alias="prompt_wav_record_url")
    instruct_text: str = Field(..., alias="instruct_text")
    stream: bool = Field(..., alias="stream")
    seed: int = Field(..., alias="seed")
    speed: float = Field(..., alias="speed")
    api_name: str = Field(..., alias="api_name")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "client_url": Description(
            en="URL of the CosyVoice Gradio web UI",
            ja="CosyVoice Gradio WebUIのURL",
        ),
        "mode_checkbox_group": Description(
            en="Mode checkbox group value",
            ja="モードチェックボックスグループの値",
        ),
        "sft_dropdown": Description(
            en="SFT dropdown value", ja="SFTドロップダウンの値"
        ),
        "prompt_text": Description(en="Prompt text", ja="プロンプトテキスト"),
        "prompt_wav_upload_url": Description(
            en="URL for prompt WAV file upload",
            ja="プロンプトWAVファイルのアップロード先URL",
        ),
        "prompt_wav_record_url": Description(
            en="URL for prompt WAV file recording",
            ja="プロンプトWAVファイルの録音先URL",
        ),
        "instruct_text": Description(en="Instruction text", ja="指示テキスト"),
        "stream": Description(en="Streaming inference", ja="ストリーミング推論"),
        "seed": Description(en="Random seed", ja="乱数シード"),
        "speed": Description(en="Speech speed multiplier", ja="発話速度の倍率"),
        "api_name": Description(en="API endpoint name", ja="APIエンドポイント名"),
    }


class MeloTTSConfig(I18nMixin):
    """Configuration for Melo TTS."""

    speaker: str = Field(..., alias="speaker")
    language: str = Field(..., alias="language")
    device: str = Field("auto", alias="device")
    speed: float = Field(1.0, alias="speed")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "speaker": Description(
            en="Speaker name (e.g., EN-Default, ZH)",
            ja="話者名（例: EN-Default、ZH）",
        ),
        "language": Description(
            en="Language code (e.g., EN, ZH)",
            ja="言語コード（例: EN、ZH）",
        ),
        "device": Description(
            en="Device to use (auto, cpu, cuda, cuda:0, mps)",
            ja="使用するデバイス（auto、cpu、cuda、cuda:0、mps）",
        ),
        "speed": Description(en="Speech speed multiplier", ja="発話速度の倍率"),
    }


class XTTSConfig(I18nMixin):
    """Configuration for XTTS."""

    api_url: str = Field(..., alias="api_url")
    speaker_wav: str = Field(..., alias="speaker_wav")
    language: str = Field(..., alias="language")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "api_url": Description(
            en="URL of the XTTS API endpoint",
            ja="XTTS APIエンドポイントのURL",
        ),
        "speaker_wav": Description(
            en="Speaker reference WAV file",
            ja="話者リファレンスWAVファイル",
        ),
        "language": Description(
            en="Language code (e.g., en, zh)",
            ja="言語コード（例: en、zh）",
        ),
    }


class GPTSoVITSConfig(I18nMixin):
    """Configuration for GPT-SoVITS."""

    api_url: str = Field(..., alias="api_url")
    text_lang: str = Field(..., alias="text_lang")
    ref_audio_path: str = Field(..., alias="ref_audio_path")
    prompt_lang: str = Field(..., alias="prompt_lang")
    prompt_text: str = Field(..., alias="prompt_text")
    text_split_method: str = Field(..., alias="text_split_method")
    batch_size: str = Field(..., alias="batch_size")
    media_type: str = Field(..., alias="media_type")
    streaming_mode: str = Field(..., alias="streaming_mode")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "api_url": Description(
            en="URL of the GPT-SoVITS API endpoint",
            ja="GPT-SoVITS APIエンドポイントのURL",
        ),
        "text_lang": Description(
            en="Language of the input text", ja="入力テキストの言語"
        ),
        "ref_audio_path": Description(
            en="Path to reference audio file",
            ja="リファレンス音声ファイルへのパス",
        ),
        "prompt_lang": Description(en="Language of the prompt", ja="プロンプトの言語"),
        "prompt_text": Description(en="Prompt text", ja="プロンプトテキスト"),
        "text_split_method": Description(
            en="Method for splitting text",
            ja="テキスト分割方法",
        ),
        "batch_size": Description(
            en="Batch size for processing", ja="処理のバッチサイズ"
        ),
        "media_type": Description(en="Output media type", ja="出力メディアタイプ"),
        "streaming_mode": Description(
            en="Enable streaming mode", ja="ストリーミングモードを有効にする"
        ),
    }


class CoquiTTSConfig(I18nMixin):
    """Configuration for Coqui TTS."""

    model_name: str = Field(..., alias="model_name")
    speaker_wav: str = Field("", alias="speaker_wav")
    language: str = Field(..., alias="language")
    device: str = Field("", alias="device")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "model_name": Description(
            en="Name of the TTS model to use",
            ja="使用するTTSモデルの名前",
        ),
        "speaker_wav": Description(
            en="Path to speaker WAV file for voice cloning",
            ja="音声クローニング用の話者WAVファイルへのパス",
        ),
        "language": Description(
            en="Language code (e.g., en, zh)",
            ja="言語コード（例: en、zh）",
        ),
        "device": Description(
            en="Device to use (cuda, cpu, or empty for auto)",
            ja="使用するデバイス（cuda、cpu、自動判定の場合は空欄）",
        ),
    }


class SherpaOnnxTTSConfig(I18nMixin):
    """Configuration for Sherpa Onnx TTS."""

    vits_model: str = Field(..., alias="vits_model")
    vits_lexicon: Optional[str] = Field(None, alias="vits_lexicon")
    vits_tokens: str = Field(..., alias="vits_tokens")
    vits_data_dir: Optional[str] = Field(None, alias="vits_data_dir")
    vits_dict_dir: Optional[str] = Field(None, alias="vits_dict_dir")
    tts_rule_fsts: Optional[str] = Field(None, alias="tts_rule_fsts")
    max_num_sentences: int = Field(2, alias="max_num_sentences")
    sid: int = Field(1, alias="sid")
    provider: Literal["cpu", "cuda", "coreml"] = Field("cpu", alias="provider")
    num_threads: int = Field(1, alias="num_threads")
    speed: float = Field(1.0, alias="speed")
    debug: bool = Field(False, alias="debug")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "vits_model": Description(
            en="Path to VITS model file", ja="VITSモデルファイルへのパス"
        ),
        "vits_lexicon": Description(
            en="Path to lexicon file (optional)",
            ja="辞書ファイルへのパス（任意）",
        ),
        "vits_tokens": Description(
            en="Path to tokens file", ja="トークンファイルへのパス"
        ),
        "vits_data_dir": Description(
            en="Path to espeak-ng data directory (optional)",
            ja="espeak-ngデータディレクトリへのパス（任意）",
        ),
        "vits_dict_dir": Description(
            en="Path to Jieba dictionary directory (optional)",
            ja="Jieba辞書ディレクトリへのパス（任意）",
        ),
        "tts_rule_fsts": Description(
            en="Path to rule FSTs file (optional)",
            ja="ルールFSTsファイルへのパス（任意）",
        ),
        "max_num_sentences": Description(
            en="Maximum number of sentences per batch",
            ja="バッチあたりの最大文数",
        ),
        "sid": Description(
            en="Speaker ID for multi-speaker models",
            ja="マルチスピーカーモデルの話者ID",
        ),
        "provider": Description(
            en="Computation provider (cpu, cuda, or coreml)",
            ja="計算プロバイダー（cpu、cuda、またはcoreml）",
        ),
        "num_threads": Description(
            en="Number of computation threads", ja="計算に使用するスレッド数"
        ),
        "speed": Description(en="Speech speed multiplier", ja="発話速度の倍率"),
        "debug": Description(en="Enable debug mode", ja="デバッグモードを有効にする"),
    }


class OpenAITTSConfig(I18nMixin):
    """Configuration for OpenAI-compatible TTS client."""

    model: Optional[str] = Field(None, alias="model")
    voice: Optional[str] = Field(None, alias="voice")
    api_key: Optional[str] = Field(None, alias="api_key")
    base_url: Optional[str] = Field(None, alias="base_url")
    file_extension: Literal["mp3", "wav"] = Field("mp3", alias="file_extension")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "model": Description(
            en="Model name for the TTS server (overrides default)",
            ja="TTSサーバーのモデル名（デフォルトを上書き）",
        ),
        "voice": Description(
            en="Voice name(s) for the TTS server (overrides default)",
            ja="TTSサーバーの音声名（デフォルトを上書き）",
        ),
        "api_key": Description(
            en="API key if required by the TTS server (overrides default)",
            ja="TTSサーバーが要求する場合のAPIキー（デフォルトを上書き）",
        ),
        "base_url": Description(
            en="Base URL of the TTS server (overrides default)",
            ja="TTSサーバーのベースURL（デフォルトを上書き）",
        ),
        "file_extension": Description(
            en="Audio file format (mp3 or wav, defaults to mp3)",
            ja="音声ファイル形式（mp3またはwav、デフォルトはmp3）",
        ),
    }


class SparkTTSConfig(I18nMixin):
    """Configuration for Spark TTS."""

    api_url: str = Field(..., alias="api_url")
    prompt_wav_upload: str = Field(..., alias="prompt_wav_upload")
    api_name: str = Field(..., alias="api_name")
    gender: str = Field(..., alias="gender")
    pitch: int = Field(..., alias="pitch")
    speed: int = Field(..., alias="speed")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "prompt_wav_upload": Description(
            en="Reference audio (used when using voice cloning)",
            ja="リファレンス音声（ボイスクローニング使用時に使用）",
        ),
        "api_url": Description(
            en="API address of the spark tts gradio web frontend. For example: http://127.0.0.1:7860/voice_clone",
            ja="Spark TTS Gradio WebフロントエンドのAPIアドレス。例: http://127.0.0.1:7860/voice_clone",
        ),
        "api_name": Description(
            en="The API endpoint name. For example: voice_clone,voice_creation",
            ja="APIエンドポイント名。例: voice_clone、voice_creation",
        ),
        "gender": Description(
            en="Gender of the voice (male or female)",
            ja="音声の性別（maleまたはfemale）",
        ),
        "pitch": Description(
            en="Pitch shift (in semitones) default 3,range 1-5.",
            ja="ピッチシフト（半音単位）デフォルト3、範囲1〜5。",
        ),
        "speed": Description(
            en="Speed of the voice (in percent) default 3,range 1-5.",
            ja="音声の速度（パーセント）デフォルト3、範囲1〜5。",
        ),
    }


class PiperTTSConfig(I18nMixin):
    """Configuration for Piper TTS."""

    model_path: str = Field("models/piper/zh_CN-huayan-medium.onnx", alias="model_path")
    speaker_id: int = Field(0, alias="speaker_id")
    length_scale: float = Field(1.0, alias="length_scale")
    noise_scale: float = Field(0.667, alias="noise_scale")
    noise_w: float = Field(0.8, alias="noise_w")
    volume: float = Field(1.0, alias="volume")
    normalize_audio: bool = Field(True, alias="normalize_audio")
    use_cuda: bool = Field(False, alias="use_cuda")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "model_path": Description(
            en="Path to Piper ONNX model file",
            ja="Piper ONNXモデルファイルへのパス",
        ),
        "speaker_id": Description(
            en="Speaker ID for multi-speaker models (default 0 for single-speaker)",
            ja="マルチスピーカーモデルの話者ID（シングルスピーカーの場合はデフォルト0）",
        ),
        "length_scale": Description(
            en="Speech speed control (0.5=2x faster, 1.0=normal, 2.0=2x slower)",
            ja="発話速度の制御（0.5=2倍速、1.0=通常、2.0=1/2速）",
        ),
        "noise_scale": Description(
            en="Audio variation degree (0.0-1.0, higher=more varied)",
            ja="音声のばらつき度合い（0.0〜1.0、値が大きいほど多様）",
        ),
        "noise_w": Description(
            en="Speaking style variation (0.0-1.0, higher=more diverse)",
            ja="話し方のスタイルのばらつき（0.0〜1.0、値が大きいほど多様）",
        ),
        "volume": Description(
            en="Output volume (0.0-1.0, 1.0=normal)",
            ja="出力音量（0.0〜1.0、1.0=通常）",
        ),
        "normalize_audio": Description(
            en="Whether to normalize audio output (recommended)",
            ja="出力音声を正規化するかどうか（推奨）",
        ),
        "use_cuda": Description(
            en="Whether to use GPU acceleration (requires onnxruntime-gpu)",
            ja="GPUアクセラレーションを使用するかどうか（onnxruntime-gpuが必要）",
        ),
    }


class KokoroTTSConfig(I18nMixin):
    """Configuration for Kokoro TTS (kokoro-onnx)."""

    model_path: str = Field("models/kokoro/kokoro-v1.0.onnx", alias="model_path")
    voices_path: str = Field("models/kokoro/voices-v1.0.bin", alias="voices_path")
    voice: str = Field("jf_alpha", alias="voice")
    speed: float = Field(1.0, alias="speed")
    lang: Literal["ja"] = Field("ja", alias="lang")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "model_path": Description(
            en="Path to Kokoro ONNX model file (kokoro-v1.0.onnx)",
            ja="Kokoro ONNXモデルファイルへのパス（kokoro-v1.0.onnx）",
        ),
        "voices_path": Description(
            en="Path to Kokoro voices file (voices-v1.0.bin)",
            ja="Kokoroボイスファイルへのパス（voices-v1.0.bin）",
        ),
        "voice": Description(
            en="Voice name (e.g., af_sarah, af_heart, jf_alpha for Japanese)",
            ja="ボイス名（例: af_sarah、af_heart、日本語はjf_alpha）",
        ),
        "speed": Description(
            en="Speech speed (1.0=normal)",
            ja="発話速度（1.0=通常）",
        ),
        "lang": Description(
            en="Language code (e.g., en-us, ja)",
            ja="言語コード（例: en-us、ja）",
        ),
    }


TTSModelName = Literal[
    "bark_tts",
    "cosyvoice_tts",
    "cosyvoice2_tts",
    "melo_tts",
    "coqui_tts",
    "x_tts",
    "gpt_sovits_tts",
    "sherpa_onnx_tts",
    "openai_tts",
    "spark_tts",
    "piper_tts",
    "kokoro_tts",
]


class TTSConfig(I18nMixin):
    """Configuration for Text-to-Speech."""

    tts_model: TTSModelName = Field(..., alias="tts_model")
    # Used when the main engine fails, e.g. the GPT-SoVITS server is not running.
    fallback_tts_model: Optional[TTSModelName] = Field(None, alias="fallback_tts_model")

    bark_tts: Optional[BarkTTSConfig] = Field(None, alias="bark_tts")
    cosyvoice_tts: Optional[CosyvoiceTTSConfig] = Field(None, alias="cosyvoice_tts")
    cosyvoice2_tts: Optional[Cosyvoice2TTSConfig] = Field(None, alias="cosyvoice2_tts")
    melo_tts: Optional[MeloTTSConfig] = Field(None, alias="melo_tts")
    coqui_tts: Optional[CoquiTTSConfig] = Field(None, alias="coqui_tts")
    x_tts: Optional[XTTSConfig] = Field(None, alias="x_tts")
    gpt_sovits_tts: Optional[GPTSoVITSConfig] = Field(None, alias="gpt_sovits")
    sherpa_onnx_tts: Optional[SherpaOnnxTTSConfig] = Field(
        None, alias="sherpa_onnx_tts"
    )
    openai_tts: Optional[OpenAITTSConfig] = Field(None, alias="openai_tts")
    spark_tts: Optional[SparkTTSConfig] = Field(None, alias="spark_tts")
    piper_tts: Optional[PiperTTSConfig] = Field(None, alias="piper_tts")
    kokoro_tts: Optional[KokoroTTSConfig] = Field(None, alias="kokoro_tts")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "tts_model": Description(
            en="Text-to-speech model to use",
            ja="使用する音声合成（TTS）モデル",
        ),
        "bark_tts": Description(en="Configuration for Bark TTS", ja="Bark TTSの設定"),
        "cosyvoice_tts": Description(
            en="Configuration for Cosyvoice TTS",
            ja="Cosyvoice TTSの設定",
        ),
        "cosyvoice2_tts": Description(
            en="Configuration for Cosyvoice2 TTS",
            ja="Cosyvoice2 TTSの設定",
        ),
        "melo_tts": Description(en="Configuration for Melo TTS", ja="Melo TTSの設定"),
        "coqui_tts": Description(
            en="Configuration for Coqui TTS", ja="Coqui TTSの設定"
        ),
        "x_tts": Description(en="Configuration for XTTS", ja="XTTSの設定"),
        "gpt_sovits_tts": Description(
            en="Configuration for GPT-SoVITS",
            ja="GPT-SoVITSの設定",
        ),
        "sherpa_onnx_tts": Description(
            en="Configuration for Sherpa Onnx TTS",
            ja="Sherpa Onnx TTSの設定",
        ),
        "openai_tts": Description(
            en="Configuration for OpenAI-compatible TTS",
            ja="OpenAI互換TTSの設定",
        ),
        "spark_tts": Description(
            en="Configuration for Spark TTS", ja="Spark TTSの設定"
        ),
        "piper_tts": Description(
            en="Configuration for Piper TTS", ja="Piper TTSの設定"
        ),
        "kokoro_tts": Description(
            en="Configuration for Kokoro TTS", ja="Kokoro TTSの設定"
        ),
    }

    @model_validator(mode="after")
    def check_tts_config(cls, values: "TTSConfig", info: ValidationInfo):
        # The selected TTS model must come with its config block
        if getattr(values, values.tts_model, None) is None:
            raise ValueError(
                f"tts_model is set to '{values.tts_model}' but the "
                f"'{values.tts_model}' configuration block is missing"
            )
        fallback = values.fallback_tts_model
        if fallback and getattr(values, fallback, None) is None:
            raise ValueError(
                f"fallback_tts_model is set to '{fallback}' but the "
                f"'{fallback}' configuration block is missing"
            )
        return values
