from typing import Any
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    BASE_KEYS: list[str] = Field(
        env='BASE_KEYS',
        default=[
            '9YPu863p-251JwL6M-p375kd6m',
'qt513k6O-2T1b63LR-tz526uQ8',
'A04Z2qv7-23xZ68KU-3pTF02i6',
'L4d5N13K-16V78RPg-tg807l2i',
'sx28Dd19-S8o67U5d-j6wH4g83',
'o54j2R0Y-a0g58Dz1-7Y96a5Hg',
'zK3r246f-m98N0Oj5-c5O341bB',
'n7tmF586-r2kc983e-23i9lw7E',
'70PYzp86-b35Rl27I-9q724MhA',
'02S97jDr-517GKI6e-Zo18f9H4',
'74V6p5Ew-785jl0sP-8P3Yn7o2',
        ]
    )
    THREADS_COUNT: int = Field(env='THREADS_COUNT', default=1)
    PROXY_FILE: str | None = Field(env='PROXY_FILE', default=None)
    DEVICE_MODELS: list[str] = Field(env='DEVICE_MODELS', default=[])
    DELAY: int = Field(env='DELAY', default=25)
    OUTPUT_FILE: str = Field(env='OUTPUT_FILE', default='output.txt')
    OUTPUT_FORMAT: str = Field(env='OUTPUT_FORMAT', default='{key} | {referral_count}')
    RETRY_COUNT: int = Field(env='RETRY_COUNT', default=3)

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

        @classmethod
        def parse_env_var(cls, field: str, raw_val: str) -> Any:
            if field == 'BASE_KEYS' or field == 'DEVICE_MODELS':
                if isinstance(raw_val, str):
                    return str(raw_val).split(',')

            return cls.json_loads(raw_val) # type: ignore

config = Settings()
