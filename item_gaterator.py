import random

from enums.action_enums import ActionEnum
from enums.item_enums import ItemsEnum


class Item:

    @staticmethod
    def select_action():
        return random.choice(list(ActionEnum))

    @staticmethod
    def select_item():
        return random.choice(list(ItemsEnum))

    @staticmethod
    def sword():
        sword = random.randint(10, 100)
        return sword

    # другие объекты
