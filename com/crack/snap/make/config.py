# @author Mohan Sharma
from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    base_url: str = ''
    wait_time_in_secs: int = 20
    http_timeout: float = 10.0
    http_max_keepalive_connections: int = 10
    http_max_connections: int = 100
    
    model_config = SettingsConfigDict(env_file=".env")


class DevSettings(CommonSettings):
    model_config = SettingsConfigDict(env_file=".env.dev")


class ProdSettings(CommonSettings):
    model_config = SettingsConfigDict(env_file=".env.prod")


def get_settings(env: str):
    if env == "dev":
        return DevSettings()
    elif env == "prod":
        return ProdSettings()
    else:
        raise ValueError(f"Invalid environment: {env}")
