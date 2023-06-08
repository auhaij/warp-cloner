from typing import Any
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    BASE_KEYS: list[str] = Field(
        env='BASE_KEYS',
        default=[
'1N6BU95g-9Uw61L3I-L1S4D2i7',
'39M1vda7-c9s2e3T7-t29Qq80r',
'8xRcY412-1vSa640I-PycH0528',
'7t0bm96L-M3J81Z0n-Z428nBd0',
'3Eke51U2-J93Ns8o5-mO5q13o9',
'76e5nf3v-t72KA10e-iAx206I7',
'p63YZ5D1-8D1P5B2o-43te5s2Z',
'6idW3o57-078xM9Ty-513Qh7Ot',
'E3Ss8Q06-AE2058kf-50V34ZAu',
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
