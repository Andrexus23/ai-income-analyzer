from pydantic_settings import BaseSettings, JsonConfigSettingsSource
from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    JsonConfigSettingsSource,
)

class LLMSettings(BaseModel):
    """Settings for model interaction."""

    api_base: str
    model: str
    
class VectorStoreSettings(BaseModel):
    """Settings for vector store interaction."""

    db_path: str
    embeddings_model: str
    
class DataSettings(BaseModel):
    """Data settings."""
    
    dataset_path: str


class Settings(BaseSettings):

    llm_settings: LLMSettings
    vector_store_settings: VectorStoreSettings
    data_settings: DataSettings
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