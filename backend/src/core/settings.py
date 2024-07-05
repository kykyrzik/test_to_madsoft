from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

PATH_TO_HOME = Path(__file__).parent.parent.parent


class DBSetting(BaseSettings):
    model_config = SettingsConfigDict(env_file=f'{PATH_TO_HOME}/.env',
                                      env_prefix='DB_',
                                      case_sensitive=False,
                                      extra='ignore')
    user: Optional[str] = None
    port: Optional[int] = None
    host: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    uri: Optional[str] = None

    @property
    def get_url(self) -> str:
        if self.uri is None:
            raise AttributeError(f'URI not set for {self.__class__.__name__}')
        return self.uri.format(user=self.user,
                               password=self.password,
                               host=self.host,
                               port=self.port,
                               name=self.name
                               )


class APISetting(BaseSettings):
    model_config = SettingsConfigDict(env_file=f'{PATH_TO_HOME}/.env',
                                      env_prefix='API_',
                                      case_sensitive=False,
                                      extra='ignore')
    host: str = "127.0.0.1"
    port: int = 8001


class Settings(BaseSettings):
    db_setting: DBSetting = DBSetting()
    api_setting: APISetting = APISetting()


def load_setting() -> Settings:
    return Settings()
