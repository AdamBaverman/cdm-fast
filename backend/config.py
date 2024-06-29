import os

class Settings:
    MONGO_URL: str = os.getenv("MONGO_URL", "mongodb://mongo:27017")

settings = Settings()
