import json
from python_widget.LastfiveTransactions import Transactions


def load_information(filename):
    """
    Загружает данные с внешнего источника
    :param filename: Имя файла в формате '.JSON'
    :return: Возвращает данные в формате словаря для работы в Python
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_filtered_data(data, last_operations=5):
    """
    Фильтрует и сортирует словарь по дате и выводит указанное количество записей
    :param data: Имя файла с данными в виде словаря Python
    :param last_five: Аргумент количества вывода последних операций
    :return: Возвращает указанное количество последних упешных банковских операций в виде словаря
    """
    data = [item for item in data if 'state' in item and item['state'] == 'EXECUTED']
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    return sorted_data[:last_operations]


def creates_instance_Transactions(data):
    """
    Создает экземпляр класса Transactions
    :param data: Имя файла с данными в виде словаря Python
    :return: Возвращает список экземпляров класса Transactions
    """
    instances = []
    for item in data:
        date = item['date']
        description = item['description']
        amount = item['operationAmount']['amount'] if 'amount' in item['operationAmount'] else ''
        currency_name = item['operationAmount']['currency']['name'] if 'name' in item['operationAmount']['currency'] else ''
        from_account = item['from'] if 'from' in item else ''
        to_account = item['to'] if 'to' in item else ''
        instance = Transactions(date, description, amount, currency_name, from_account, to_account)
        instances.append(instance)
    return instances
