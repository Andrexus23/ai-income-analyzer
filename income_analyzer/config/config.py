from pydantic_settings import BaseSettings, JsonConfigSettingsSource
from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    JsonConfigSettingsSource,
)

class ModelSettings(BaseModel):
    """Settings for model interaction."""

    api_base: str
    model: str


class Settings(BaseSettings):

    dataset: str
    model_settings: ModelSettings
    model_config = SettingsConfigDict(json_file='config.json')
    
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """"""
        return (JsonConfigSettingsSource(settings_cls),)


def get_config() -> Settings:
    """Get settings from config."""
    return Settings()