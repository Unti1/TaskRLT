from settings import *

command_router = Router()

# @command_router.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Отправьте мне JSON с входными данными.")

# @command_router.message_handler()
# async def aggregate(message: types.Message):
#     from tools.db_agregator import aggregate_salaries

#     try:
#         input_data = json.loads(message.text)
#         result = await aggregate_salaries(**input_data)
#         await message.answer(json.dumps(result, ensure_ascii=False))
#     except (json.JSONDecodeError, KeyError):
#         await message.reply("Пожалуйста, отправьте корректный JSON.")