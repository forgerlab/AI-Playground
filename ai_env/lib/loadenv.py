from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    hf_token: str
    openai_api_key: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()