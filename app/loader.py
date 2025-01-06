from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from config import settings

bot = Bot(
    token=settings.TELEGRAM_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML, protect_content=settings.PROTECT_CONTENT
    ),
)
dispatcher = Dispatcher(disable_fsm=True)
