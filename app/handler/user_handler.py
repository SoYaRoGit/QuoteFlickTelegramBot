from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    await message.delete()
    await message.answer(text="Бот успешно работает")
