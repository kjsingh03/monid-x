from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    monid_api_key: str
    groq_api_key: str
    monid_base_url: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
