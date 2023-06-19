class Transactions:
    def __init__(self, date, description, amount, currency_name, from_account=None, to_account=None, ):
        self.date = date
        self.description = description
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.currency_name = currency_name

    def __repr__(self):
        return f'{self.date, self.amount}\n' \
               f'{self.description, self.from_account, self.to_account}'

    def return_secret_number(self, account):
        """
        Функция шифрует номер счета/карты
        :param account: Получает номер счета
        :return: Возвращает зашифрованный номер счета
        """
        if account is None:
            return ''
        else:
            count = 0
            card_number = ''
            hide_number = ''
            if 'Счет' in account:
                card_number = account.split()[-1]
                hide_number = len(card_number[-6:-4]) * '*' + card_number[-4:]
                return f'{account.split()[-2]} {hide_number}'
            else:
                for digit in account:
                    if digit.isdigit():
                        card_number += digit
                        count += 1
                    if count == 4:
                        card_number += ' '
                        count = 0
                for index, num in enumerate(card_number):
                    if 7 <= index < 14 and num.isdigit():
                        hide_number += '*'
                    else:
                        hide_number += num

                return f'{account[:-17]} {hide_number}'

    def return_secret_number_from(self):
        """
        :return: Возвращает зашифрованный номер отправителя
        """
        return self.return_secret_number(self.from_account)

    def return_secret_number_to(self):
        """
        :return: Возвращает зашифрованный номер получателя
        """
        return self.return_secret_number(self.to_account)

    def return_date(self):
        """
        :return: Возвращает дату в формате str
        """
        return f'{self.date}'

    def return_description(self):
        """
        :return: Возвращает описание перевода
        """
        return f'{self.description}'

    def return_amount_and_currency(self):
        """
        :return: Возвращает сумму операции "amount" и наименование валюты в которой была совершена операция "currency_name"
        """
        return f'{self.amount} {self.currency_name}'
