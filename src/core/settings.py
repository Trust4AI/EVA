from pydantic_settings import BaseSettings

import os


class Settings(BaseSettings):

    hugging_face_api_key: str

    class Config:
        extra = "allow"
        env_file = os.path.join(os.path.dirname(__file__), '../../.env')
        env_file_encoding = "utf-8"

settings = Settings()
