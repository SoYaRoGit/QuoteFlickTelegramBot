from typing import Any, Dict

from pydantic import field_validator
from pydantic_settings import BaseSettings
from requests import Response, get


class Settings(BaseSettings):
    # Телеграм бот API
    TELEGRAM_TOKEN: str

    # Защита от скриншотов и копирования
    PROTECT_CONTENT: bool

    @field_validator("TELEGRAM_TOKEN", mode="before")
    @classmethod
    def verify_api(cls, token: str) -> str:
        # Проверяем на тип данных str и наличие ":"
        if not isinstance(token, str) or ":" not in token:
            raise ValueError("Неверный формат TELEGRAM_TOKEN")

        # Разделение TELEGRAM_TOKEN на две части
        id, key = token.split(":")

        # Проверяем наличие чисел в левой части
        if not id.isdigit():
            raise ValueError("Левая часть TELEGRAM_TOKEN должна быть числовой")

        # Проверка наличия правой части
        if not key:
            raise ValueError("Правая часть TELEGRAM_TOKEN не должен пустовать")

        url: str = f"https://api.telegram.org/bot{token}/getMe"
        response: Response = get(url)
        data: Dict[str, Any] = response.json()

        if not data.get("ok", False):
            raise ValueError(
                "Telegram API вернул ошибку при попытке соединиться с ботом."
            )

        return token


settings = Settings()
