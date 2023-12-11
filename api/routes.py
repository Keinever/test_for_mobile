from enum import Enum


class Routes(str, Enum):
    INFO = '/info'
    OBJECTS_ITEM = '/objects/{}'
    ADD_ACTION = '/addAction'
    GET_USER_ACTION = '/getUserActions'
    REPLENISH_BALANCE = '/replenishBalance'
    GET_ACTIONS = '/getActions'
    SELL_ACTION = '/sellAction'
    AUTH = '/auth'
    REG = '/reg'

    def __str__(self) -> str:
        return self.value
