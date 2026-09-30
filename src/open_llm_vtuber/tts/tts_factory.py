from typing import Type
from .tts_interface import TTSInterface


class TTSFactory:
    @staticmethod
    def get_tts_engine(engine_type, **kwargs) -> Type[TTSInterface]:
        if engine_type == "bark_tts":
            from .bark_tts import TTSEngine as BarkTTSEngine

            return BarkTTSEngine(kwargs.get("voice"))
        elif engine_type == "cosyvoice_tts":
            from .cosyvoice_tts import TTSEngine as CosyvoiceTTSEngine

            return CosyvoiceTTSEngine(
                client_url=kwargs.get("client_url"),
                mode_checkbox_group=kwargs.get("mode_checkbox_group"),
                sft_dropdown=kwargs.get("sft_dropdown"),
                prompt_text=kwargs.get("prompt_text"),
                prompt_wav_upload_url=kwargs.get("prompt_wav_upload_url"),
                prompt_wav_record_url=kwargs.get("prompt_wav_record_url"),
                instruct_text=kwargs.get("instruct_text"),
                seed=kwargs.get("seed"),
                api_name=kwargs.get("api_name"),
            )
        elif engine_type == "cosyvoice2_tts":
            from .cosyvoice2_tts import TTSEngine as Cosyvoice2TTSEngine

            return Cosyvoice2TTSEngine(
                client_url=kwargs.get("client_url"),
                mode_checkbox_group=kwargs.get("mode_checkbox_group"),
                sft_dropdown=kwargs.get("sft_dropdown"),
                prompt_text=kwargs.get("prompt_text"),
                prompt_wav_upload_url=kwargs.get("prompt_wav_upload_url"),
                prompt_wav_record_url=kwargs.get("prompt_wav_record_url"),
                instruct_text=kwargs.get("instruct_text"),
                stream=kwargs.get("stream"),
                seed=kwargs.get("seed"),
                speed=kwargs.get("speed"),
                api_name=kwargs.get("api_name"),
            )
        elif engine_type == "melo_tts":
            from .melo_tts import TTSEngine as MeloTTSEngine

            return MeloTTSEngine(
                speaker=kwargs.get("speaker"),
                language=kwargs.get("language"),
                device=kwargs.get("device"),
                speed=kwargs.get("speed"),
            )
        elif engine_type == "x_tts":
            from .x_tts import TTSEngine as XTTSEngine

            return XTTSEngine(
                api_url=kwargs.get("api_url"),
                speaker_wav=kwargs.get("speaker_wav"),
                language=kwargs.get("language"),
            )
        elif engine_type == "gpt_sovits_tts":
            from .gpt_sovits_tts import TTSEngine as GSVEngine

            return GSVEngine(
                api_url=kwargs.get("api_url"),
                text_lang=kwargs.get("text_lang"),
                ref_audio_path=kwargs.get("ref_audio_path"),
                prompt_lang=kwargs.get("prompt_lang"),
                prompt_text=kwargs.get("prompt_text"),
                text_split_method=kwargs.get("text_split_method"),
                batch_size=kwargs.get("batch_size"),
                media_type=kwargs.get("media_type"),
                streaming_mode=kwargs.get("streaming_mode"),
            )
        elif engine_type == "coqui_tts":
            from .coqui_tts import TTSEngine as CoquiTTSEngine

            return CoquiTTSEngine(
                model_name=kwargs.get("model_name"),
                speaker_wav=kwargs.get("speaker_wav"),
                language=kwargs.get("language"),
                device=kwargs.get("device"),
            )

        elif engine_type == "sherpa_onnx_tts":
            from .sherpa_onnx_tts import TTSEngine as SherpaOnnxTTSEngine

            return SherpaOnnxTTSEngine(**kwargs)
        elif engine_type == "openai_tts":
            from .openai_tts import TTSEngine as OpenAITTSEngine

            # Pass relevant config options, allowing defaults in openai_tts.py if not provided
            return OpenAITTSEngine(
                model=kwargs.get("model"),  # Will use default "kokoro" if not in kwargs
                voice=kwargs.get(
                    "voice"
                ),  # Will use default "af_sky+af_bella" if not in kwargs
                api_key=kwargs.get(
                    "api_key"
                ),  # Will use default "not-needed" if not in kwargs
                base_url=kwargs.get(
                    "base_url"
                ),  # Will use default "http://localhost:8880/v1" if not in kwargs
                file_extension=kwargs.get(
                    "file_extension"
                ),  # Will use default "mp3" if not in kwargs
            )

        elif engine_type == "spark_tts":
            from .spark_tts import TTSEngine as SparkTTSEngine

            return SparkTTSEngine(
                api_url=kwargs.get("api_url"),
                prompt_wav_upload=kwargs.get("prompt_wav_upload"),
                api_name=kwargs.get("api_name"),
                gender=kwargs.get("gender"),
                pitch=kwargs.get("pitch"),
                speed=kwargs.get("speed"),
            )
        elif engine_type == "piper_tts":
            from .piper_tts import TTSEngine as PiperTTSEngine

            return PiperTTSEngine(
                model_path=kwargs.get("model_path"),
                speaker_id=kwargs.get("speaker_id"),
                length_scale=kwargs.get("length_scale"),
                noise_scale=kwargs.get("noise_scale"),
                noise_w=kwargs.get("noise_w"),
                volume=kwargs.get("volume"),
                normalize_audio=kwargs.get("normalize_audio"),
                use_cuda=kwargs.get("use_cuda"),
            )
        elif engine_type == "kokoro_tts":
            from .kokoro_tts import TTSEngine as KokoroTTSEngine

            return KokoroTTSEngine(**kwargs)
        else:
            raise ValueError(f"Unknown TTS engine type: {engine_type}")
