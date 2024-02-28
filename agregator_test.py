import pytest
from tools.db_agregator import aggregate_salaries

# Обратите внимание на добавление квадратных скобок, чтобы создать список кортежей для parametrize
@pytest.mark.parametrize("dt_from, dt_upto, group_type, expected", [
    ("2022-09-01T00:00:00", "2022-12-31T23:59:00", "month", {
        'dataset': [5906586, 5515874, 5889803, 6092634],
        'labels': ['2022-09-01T00:00:00', '2022-10-01T00:00:00', '2022-11-01T00:00:00', '2022-12-01T00:00:00']
    }),
])
async def test_salaries_aggregator(dt_from, dt_upto, group_type, expected):
    result = await aggregate_salaries(dt_from, dt_upto, group_type)
    assert result == expected
