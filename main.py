from settings import *
from handlers.commands import command_router
from handlers.agregators import agre_router


async def main_run():
    bot = Bot(token = config['tg']['token'], parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(command_router, agre_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main_run())
