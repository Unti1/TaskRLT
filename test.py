from tools.db_agregator import aggregate_salaries
from settings import *

# Пример использования
async def main():
    input_data = {
       "dt_from": "2022-09-01T00:00:00",
       "dt_upto": "2022-12-31T23:59:00",
       "group_type": "month"
    }
    result = await aggregate_salaries(**input_data)
    print(json.dumps(result, indent=2))

asyncio.run(main())