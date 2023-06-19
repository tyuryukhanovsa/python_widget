import pytest

from python_widget.LastfiveTransactions import Transactions


@pytest.fixture
def test_data_1():
    return [
        {
            'id': 863064926,
            'state': 'EXECUTED',
            'date': '2019-12-08T22:46:21.935582',
            'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Открытие вклада',
            'to': 'Счет 90424923579946435907'
        },
        {
            'id': 114832369,
            'state': 'EXECUTED',
            'date': '2019-12-07T06:17:14.634890',
            'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации',
            'from': 'Visa Classic 2842878893689012',
            'to': 'Счет 35158586384610753655'
        },
        {
            'id': 154927927,
            'state': 'EXECUTED',
            'date': '2019-11-19T09:22:25.899614',
            'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Перевод организации',
            'from': 'Maestro 7810846596785568',
            'to': 'Счет 43241152692663622869'
        }
    ]

@pytest.fixture()
def test_data_2():
    return [Transactions('2019-12-08T22:46:21.935582', 'Открытие вклада', '41096.24', '', '', 'Счет 90424923579946435907'),
        Transactions('2019-12-07T06:17:14.634890', 'Перевод организации', '48150.39', '',
                     'Visa Classic 2842878893689012', 'Счет 35158586384610753655'),
        Transactions('2019-11-19T09:22:25.899614', 'Перевод организации', '30153.72', '', 'Maestro 7810846596785568',
                     'Счет 43241152692663622869')]