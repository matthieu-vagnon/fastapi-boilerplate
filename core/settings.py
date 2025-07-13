from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_db: str = ""
    postgres_user: str = ""
    postgres_password: str = ""
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    origins: list[str] = []

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
