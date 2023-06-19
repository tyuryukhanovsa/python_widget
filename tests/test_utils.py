import python_widget
from python_widget.LastfiveTransactions import Transactions
from python_widget.utils import get_filtered_data, creates_instance_Transactions, load_information


def test_load_information():
    data = load_information('../operations.json')
    assert isinstance(data, list)


def test_get_filtered_data(test_data_1):
    data = get_filtered_data(test_data_1, 2)
    assert len(data) == 2


def test_creates_instance_Transactions(test_data_1):
    expected_output = [
        Transactions('2019-12-08T22:46:21.935582', 'Открытие вклада', '41096.24', '', '', 'Счет 90424923579946435907'),
        Transactions('2019-12-07T06:17:14.634890', 'Перевод организации', '48150.39', '',
                     'Visa Classic 2842878893689012', 'Счет 35158586384610753655'),
        Transactions('2019-11-19T09:22:25.899614', 'Перевод организации', '30153.72', '', 'Maestro 7810846596785568',
                     'Счет 43241152692663622869')
    ]

    instances_got = creates_instance_Transactions(test_data_1)

    assert len(instances_got) == len(expected_output)

    result_expected =[]
    for item in expected_output:
        result_expected.append(item)
        return result_expected

    result_got = []
    for item in instances_got:
        result_got.append(item)
        return result_got

    assert result_expected == result_got


def test_return_secret_number_to(test_data_2):
    data = [x.return_secret_number_to() for x in test_data_2]
    assert data == ['Счет **5907', 'Счет **3655', 'Счет **2869']


def test_return_secret_number_from(test_data_2):
    data = [x.return_secret_number_from() for x in test_data_2]
    assert data == [' ', 'Visa Classic 2842 87** **** 9012 ', 'Maestro 7810 84** **** 5568 ']


def test_return_date(test_data_2):
    data = [x.return_date() for x in test_data_2]
    assert data == ['2019-12-08T22:46:21.935582', '2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614']