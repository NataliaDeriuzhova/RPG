from creature import Creature
from enums.action_enums import ActionEnum
from enums.item_enums import CreatureTypes
from helpers.helper import show_state
from item_gaterator import Item


class Action:
    def __init__(self, action_type=None):
        self.action_type = action_type

    @property
    def action(self):
        # return Item.select_action()
        return ActionEnum.FIGHT.value

    def do_action(self, knight):
        if self.action == ActionEnum.FIGHT.value:
            knight = self.fight(knight)
        elif self.action_type == ActionEnum.ITEM.value:
            pass
        elif self.action_type == ActionEnum.TOTEM.value:
            pass
        return knight

    @staticmethod
    @show_state
    def fight(knight):
        monster = Creature(hp=10, creature_type=CreatureTypes.ARCHER.value, power=6)
        knight.hp -= monster.power
        return knight
