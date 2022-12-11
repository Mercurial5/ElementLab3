from __future__ import annotations
from bank import Account, currency


class BankAccount:
    accounts: list[BankAccount] = []

    def __init__(self, name: str, surname: str, wallet: int = 0, account: Account = Account.KZT):
        self.name = name
        self.surname = surname
        self.__account = account
        self.__wallet = wallet

        self.accounts.append(self)

    def add(self, amount: int) -> bool:
        self.__wallet += amount
        return True

    def withdraw(self, amount: int) -> bool:
        if self.wallet >= amount:
            self.__wallet -= amount
            return True

        return False

    def convert(self, another_account: Account):
        self.__wallet *= currency[self.account][another_account]
        self.__account = another_account

    @staticmethod
    def get_account(name: str, surname: str) -> BankAccount | None:
        account = (account for account in BankAccount.accounts if account.name == name and account.surname == surname)

        return next(account, None)

    @property
    def wallet(self):
        return self.__wallet

    @property
    def account(self):
        return self.__account

    def __str__(self):
        return f'{self.name} {self.surname}: {self.wallet} {self.account.name}'

    def __del__(self):
        del self.name, self.surname, self.__account, self.__wallet

    # In my understanding, user cannot do this (it's like cheating)
    # so I commented this part of the code.

    # @wallet.setter
    # def wallet(self, amount: int):
    #     self.__wallet = amount

    # @account.setter
    # def account(self, new_account: Account):
    #     self.__account = new_account
