# config_manager/asr.py
from pydantic import ValidationInfo, Field, model_validator
from typing import Literal, Optional, Dict, ClassVar
from .i18n import I18nMixin, Description


class AzureASRConfig(I18nMixin):
    """Configuration for Azure ASR service."""

    api_key: str = Field(..., alias="api_key")
    region: str = Field(..., alias="region")
    languages: list[str] = Field(["en-US", "zh-CN"], alias="languages")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "api_key": Description(
            en="API key for Azure ASR service",
            ja="Azure ASRサービスのAPIキー",
        ),
        "region": Description(
            en="Azure region (e.g., eastus)",
            ja="Azureのリージョン（例: eastus）",
        ),
        "languages": Description(
            en="List of languages to detect (e.g., ['en-US', 'zh-CN'])",
            ja="検出する言語のリスト（例: ['en-US', 'zh-CN']）",
        ),
    }


class FasterWhisperConfig(I18nMixin):
    """Configuration for Faster Whisper ASR."""

    model_path: str = Field(..., alias="model_path")
    download_root: str = Field(..., alias="download_root")
    language: Optional[str] = Field(None, alias="language")
    device: str = Field("auto", alias="device")
    compute_type: Literal["int8", "float16", "float32"] = Field(
        "int8", alias="compute_type"
    )
    prompt: str | None = Field(None, alias="prompt")
    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "model_path": Description(
            en="Path to the Faster Whisper model",
            ja="Faster Whisperモデルへのパス",
        ),
        "download_root": Description(
            en="Root directory for downloading models",
            ja="モデルのダウンロード先ルートディレクトリ",
        ),
        "language": Description(
            en="Language code (e.g., en, zh) or empty string for auto-detect",
            ja="言語コード（例: en, zh）。自動検出する場合は空文字列",
        ),
        "device": Description(
            en="Device to use for inference (cpu, cuda, or auto)",
            ja="推論に使用するデバイス（cpu、cuda、またはauto）",
        ),
        "compute_type": Description(
            en="Compute type for the model (int8, float16, or float32)",
            ja="モデルの計算タイプ（int8、float16、またはfloat32）",
        ),
        "prompt": Description(
            en="An initial prompt to provide context or guide the transcription. Language of the prompt should match the audio language.",
            ja="文脈を提供したり文字起こしを誘導したりするための初期プロンプト。プロンプトの言語は音声の言語と一致させる必要があります。",
        ),
    }


class WhisperCPPConfig(I18nMixin):
    """Configuration for WhisperCPP ASR."""

    model_name: str = Field(..., alias="model_name")
    model_dir: str = Field(..., alias="model_dir")
    print_realtime: bool = Field(False, alias="print_realtime")
    print_progress: bool = Field(False, alias="print_progress")
    language: str = Field("auto", alias="language")
    prompt: str | None = Field(None, alias="prompt")
    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "model_name": Description(
            en="Name of the Whisper model",
            ja="Whisperモデルの名前",
        ),
        "model_dir": Description(
            en="Directory containing Whisper models",
            ja="Whisperモデルが格納されているディレクトリ",
        ),
        "print_realtime": Description(
            en="Print output in real-time",
            ja="出力をリアルタイムに表示する",
        ),
        "print_progress": Description(
            en="Print progress information",
            ja="進捗情報を表示する",
        ),
        "language": Description(
            en="Language code (e.g., auto, en, zh)",
            ja="言語コード（例: auto、en、zh）",
        ),
        "prompt": Description(
            en="An initial prompt to provide context or guide the transcription. Language of the prompt should match the audio language.",
            ja="文脈を提供したり文字起こしを誘導したりするための初期プロンプト。プロンプトの言語は音声の言語と一致させる必要があります。",
        ),
    }


class WhisperConfig(I18nMixin):
    """Configuration for OpenAI Whisper ASR."""

    name: str = Field(..., alias="name")
    download_root: str = Field(..., alias="download_root")
    device: Literal["cpu", "cuda"] = Field("cpu", alias="device")
    prompt: str | None = Field(None, alias="prompt")
    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "name": Description(en="Name of the Whisper model", ja="Whisperモデルの名前"),
        "download_root": Description(
            en="Root directory for downloading models",
            ja="モデルのダウンロード先ルートディレクトリ",
        ),
        "device": Description(
            en="Device to use for inference (cpu or cuda)",
            ja="推論に使用するデバイス（cpuまたはcuda）",
        ),
        "prompt": Description(
            en="An initial prompt to provide context or guide the transcription. Language of the prompt should match the audio language.",
            ja="文脈を提供したり文字起こしを誘導したりするための初期プロンプト。プロンプトの言語は音声の言語と一致させる必要があります。",
        ),
    }


class FunASRConfig(I18nMixin):
    """Configuration for FunASR."""

    model_name: str = Field("iic/SenseVoiceSmall", alias="model_name")
    vad_model: str = Field("fsmn-vad", alias="vad_model")
    punc_model: str = Field("ct-punc", alias="punc_model")
    device: Literal["cpu", "cuda"] = Field("cpu", alias="device")
    disable_update: bool = Field(True, alias="disable_update")
    ncpu: int = Field(4, alias="ncpu")
    hub: Literal["ms", "hf"] = Field("ms", alias="hub")
    use_itn: bool = Field(False, alias="use_itn")
    language: str = Field("auto", alias="language")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "model_name": Description(en="Name of the FunASR model", ja="FunASRモデルの名前"),
        "vad_model": Description(
            en="Voice Activity Detection model",
            ja="音声区間検出（VAD）モデル",
        ),
        "punc_model": Description(en="Punctuation model", ja="句読点モデル"),
        "device": Description(
            en="Device to use for inference (cpu or cuda)",
            ja="推論に使用するデバイス（cpuまたはcuda）",
        ),
        "disable_update": Description(
            en="Disable checking for FunASR updates on launch",
            ja="起動時にFunASRの更新確認を無効にする",
        ),
        "ncpu": Description(
            en="Number of CPU threads for internal operations",
            ja="内部処理に使用するCPUスレッド数",
        ),
        "hub": Description(
            en="Model hub to use (ms for ModelScope, hf for Hugging Face)",
            ja="使用するモデルハブ（ModelScopeの場合はms、Hugging Faceの場合はhf）",
        ),
        "use_itn": Description(
            en="Enable inverse text normalization",
            ja="逆テキスト正規化を有効にする",
        ),
        "language": Description(
            en="Language code (e.g., auto, zh, en)",
            ja="言語コード（例: auto、zh、en）",
        ),
    }


class GroqWhisperASRConfig(I18nMixin):
    """Configuration for Groq Whisper ASR."""

    api_key: str = Field(..., alias="api_key")
    model: str = Field("whisper-large-v3-turbo", alias="model")
    lang: Optional[str] = Field(None, alias="lang")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "api_key": Description(
            en="API key for Groq Whisper ASR",
            ja="Groq Whisper ASRのAPIキー",
        ),
        "model": Description(
            en="Name of the Groq Whisper model to use",
            ja="使用するGroq Whisperモデルの名前",
        ),
        "lang": Description(
            en="Language code (leave empty for auto-detect)",
            ja="言語コード（自動検出する場合は空欄のまま）",
        ),
    }


class SherpaOnnxASRConfig(I18nMixin):
    """Configuration for Sherpa Onnx ASR."""

    model_type: Literal[
        "transducer",
        "paraformer",
        "nemo_ctc",
        "wenet_ctc",
        "whisper",
        "tdnn_ctc",
        "sense_voice",
        "fire_red_asr",
    ] = Field(..., alias="model_type")
    encoder: Optional[str] = Field(None, alias="encoder")
    decoder: Optional[str] = Field(None, alias="decoder")
    joiner: Optional[str] = Field(None, alias="joiner")
    paraformer: Optional[str] = Field(None, alias="paraformer")
    nemo_ctc: Optional[str] = Field(None, alias="nemo_ctc")
    wenet_ctc: Optional[str] = Field(None, alias="wenet_ctc")
    tdnn_model: Optional[str] = Field(None, alias="tdnn_model")
    whisper_encoder: Optional[str] = Field(None, alias="whisper_encoder")
    whisper_decoder: Optional[str] = Field(None, alias="whisper_decoder")
    sense_voice: Optional[str] = Field(None, alias="sense_voice")
    fire_red_asr_encoder: Optional[str] = Field(None, alias="fire_red_asr_encoder")
    fire_red_asr_decoder: Optional[str] = Field(None, alias="fire_red_asr_decoder")
    tokens: str = Field(..., alias="tokens")
    num_threads: int = Field(4, alias="num_threads")
    use_itn: bool = Field(True, alias="use_itn")
    provider: Literal["cpu", "cuda", "rocm"] = Field("cpu", alias="provider")

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "model_type": Description(
            en="Type of ASR model to use",
            ja="使用するASRモデルの種類",
        ),
        "encoder": Description(
            en="Path to encoder model (for transducer)",
            ja="エンコーダーモデルへのパス（トランスデューサー用）",
        ),
        "decoder": Description(
            en="Path to decoder model (for transducer)",
            ja="デコーダーモデルへのパス（トランスデューサー用）",
        ),
        "joiner": Description(
            en="Path to joiner model (for transducer)",
            ja="ジョイナーモデルへのパス（トランスデューサー用）",
        ),
        "paraformer": Description(
            en="Path to paraformer model",
            ja="Paraformerモデルへのパス",
        ),
        "nemo_ctc": Description(en="Path to NeMo CTC model", ja="NeMo CTCモデルへのパス"),
        "wenet_ctc": Description(en="Path to WeNet CTC model", ja="WeNet CTCモデルへのパス"),
        "tdnn_model": Description(en="Path to TDNN model", ja="TDNNモデルへのパス"),
        "whisper_encoder": Description(
            en="Path to Whisper encoder model",
            ja="Whisperエンコーダーモデルへのパス",
        ),
        "whisper_decoder": Description(
            en="Path to Whisper decoder model",
            ja="Whisperデコーダーモデルへのパス",
        ),
        "sense_voice": Description(
            en="Path to SenseVoice model",
            ja="SenseVoiceモデルへのパス",
        ),
        "fire_red_asr_encoder": Description(
            en="Path to FireredASR encoder model",
            ja="FireredASRエンコーダーモデルへのパス",
        ),
        "fire_red_asr_decoder": Description(
            en="Path to FireredASR decoder model",
            ja="FireredASRデコーダーモデルへのパス",
        ),
        "tokens": Description(en="Path to tokens file", ja="トークンファイルへのパス"),
        "num_threads": Description(en="Number of threads to use", ja="使用するスレッド数"),
        "use_itn": Description(
            en="Enable inverse text normalization",
            ja="逆テキスト正規化を有効にする",
        ),
        "provider": Description(
            en="Provider for inference (cpu or cuda) (cuda option needs additional settings. Please check our docs)",
            ja="推論に使用するプロバイダー（cpuまたはcuda）（cudaオプションには追加設定が必要です。ドキュメントを確認してください）",
        ),
    }

    @model_validator(mode="after")
    def check_model_paths(cls, values: "SherpaOnnxASRConfig", info: ValidationInfo):
        model_type = values.model_type

        if model_type == "transducer":
            if not all([values.encoder, values.decoder, values.joiner, values.tokens]):
                raise ValueError(
                    "encoder, decoder, joiner, and tokens must be provided for transducer model type"
                )
        elif model_type == "paraformer":
            if not all([values.paraformer, values.tokens]):
                raise ValueError(
                    "paraformer and tokens must be provided for paraformer model type"
                )
        elif model_type == "nemo_ctc":
            if not all([values.nemo_ctc, values.tokens]):
                raise ValueError(
                    "nemo_ctc and tokens must be provided for nemo_ctc model type"
                )
        elif model_type == "wenet_ctc":
            if not all([values.wenet_ctc, values.tokens]):
                raise ValueError(
                    "wenet_ctc and tokens must be provided for wenet_ctc model type"
                )
        elif model_type == "tdnn_ctc":
            if not all([values.tdnn_model, values.tokens]):
                raise ValueError(
                    "tdnn_model and tokens must be provided for tdnn_ctc model type"
                )
        elif model_type == "whisper":
            if not all([values.whisper_encoder, values.whisper_decoder, values.tokens]):
                raise ValueError(
                    "whisper_encoder, whisper_decoder, and tokens must be provided for whisper model type"
                )
        elif model_type == "sense_voice":
            if not all([values.sense_voice, values.tokens]):
                raise ValueError(
                    "sense_voice and tokens must be provided for sense_voice model type"
                )
        elif model_type == "fire_red_asr":
            if not all(
                [
                    values.fire_red_asr_encoder,
                    values.fire_red_asr_decoder,
                    values.tokens,
                ]
            ):
                raise ValueError(
                    "fire_red_asr_encoder, fire_red_asr_decoder, and tokens must be provided for fire_red_asr model type"
                )

        return values


class ASRConfig(I18nMixin):
    """Configuration for Automatic Speech Recognition."""

    asr_model: Literal[
        "faster_whisper",
        "whisper_cpp",
        "whisper",
        "azure_asr",
        "fun_asr",
        "groq_whisper_asr",
        "sherpa_onnx_asr",
    ] = Field(..., alias="asr_model")
    azure_asr: Optional[AzureASRConfig] = Field(None, alias="azure_asr")
    faster_whisper: Optional[FasterWhisperConfig] = Field(None, alias="faster_whisper")
    whisper_cpp: Optional[WhisperCPPConfig] = Field(None, alias="whisper_cpp")
    whisper: Optional[WhisperConfig] = Field(None, alias="whisper")
    fun_asr: Optional[FunASRConfig] = Field(None, alias="fun_asr")
    groq_whisper_asr: Optional[GroqWhisperASRConfig] = Field(
        None, alias="groq_whisper_asr"
    )
    sherpa_onnx_asr: Optional[SherpaOnnxASRConfig] = Field(
        None, alias="sherpa_onnx_asr"
    )

    DESCRIPTIONS: ClassVar[Dict[str, Description]] = {
        "asr_model": Description(
            en="Speech-to-text model to use",
            ja="使用する音声認識（Speech-to-text）モデル",
        ),
        "azure_asr": Description(en="Configuration for Azure ASR", ja="Azure ASRの設定"),
        "faster_whisper": Description(
            en="Configuration for Faster Whisper",
            ja="Faster Whisperの設定",
        ),
        "whisper_cpp": Description(
            en="Configuration for WhisperCPP",
            ja="WhisperCPPの設定",
        ),
        "whisper": Description(en="Configuration for Whisper", ja="Whisperの設定"),
        "fun_asr": Description(en="Configuration for FunASR", ja="FunASRの設定"),
        "groq_whisper_asr": Description(
            en="Configuration for Groq Whisper ASR",
            ja="Groq Whisper ASRの設定",
        ),
        "sherpa_onnx_asr": Description(
            en="Configuration for Sherpa Onnx ASR",
            ja="Sherpa Onnx ASRの設定",
        ),
    }

    @model_validator(mode="after")
    def check_asr_config(cls, values: "ASRConfig", info: ValidationInfo):
        # The selected ASR model must come with its config block
        if getattr(values, values.asr_model, None) is None:
            raise ValueError(
                f"asr_model is set to '{values.asr_model}' but the "
                f"'{values.asr_model}' configuration block is missing"
            )
        return values
