import python_widget.utils
from datetime import datetime

FILE_NAME = 'operations.json'
LAST_OPERATIONS = 5


def main():
    data = python_widget.utils.load_information(FILE_NAME)
    data = python_widget.utils.get_filtered_data(data, LAST_OPERATIONS)
    data = python_widget.utils.creates_instance_Transactions(data)
    for item in data:
        date = item.return_date()
        formatted_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y') # 2019-08-26T10:50:58.294041
        print(formatted_date, item.return_description())
        if item.from_account != '':
            print(item.return_secret_number_from(), '->', item.return_secret_number_to())
        else:
            print(item.return_secret_number_to())
        print(item.return_amount_and_currency())
        print()


if __name__ == "__main__":
    main()

# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.