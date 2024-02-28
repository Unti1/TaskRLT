from settings import *

async def main_run():
    bot = Bot(token = config['tg']['token'], parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(command_router)
    
    # сохраняем список id
    bot.user_db_info = {}
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main_run(db_worker=p))