from enum import Enum


class Account(Enum):
    USD = 1
    RUB = 2
    KZT = 3
    EUR = 4


currency: dict = {
    Account.USD: {
        Account.KZT: 470,
        Account.RUB: 60,
        Account.EUR: 1
    },
    Account.KZT: {
        Account.USD: 0.002,
        Account.RUB: 0.13,
        Account.EUR: 0.002
    },
    Account.RUB: {
        Account.KZT: 7.7,
        Account.USD: 0.016,
        Account.EUR: 0.016
    },
    Account.EUR: {
        Account.KZT: 470,
        Account.RUB: 60,
        Account.USD: 1
    }
}
