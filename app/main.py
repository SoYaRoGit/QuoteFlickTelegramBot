from asyncio import run

from handler import user_handler
from loader import bot, dispatcher


@dispatcher.startup()
async def startup() -> None:
    print("Бот успешно запущен")


@dispatcher.shutdown()
async def shutdown() -> None:
    print("Бот успешно закрыл соединение")


async def main() -> None:
    dispatcher.include_router(user_handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    try:
        run(main())
    except KeyboardInterrupt:
        ...
