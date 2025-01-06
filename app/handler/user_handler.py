from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from services import api

router = Router()


@router.message(Command("jokes"))
async def command_jokes(message: Message):
    await message.delete()
    await message.answer(text=await api.jokes())


@router.message(Command("quotes"))
async def command_quotes(message: Message):
    await message.delete()
    await message.answer(text=await api.quotes())
