from pydantic_settings import BaseSettings,SettingsConfigDict #The BaseSettings Class Is Used Tp Read The Configurable Values From Envioronment Variables And The .env File. 


class Settings(BaseSettings): #Creating Our Own Configurable Class Containing The Settings Our Applications Needs To Run.
    database_url: str

    jwt_secret_key: str
    jwt_algorithm: str ="HS256"
    jwt_access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings() #Creating An Object Of The Settings Class Which Will Be Used To Access The Configurable Values Throughout The Application.

