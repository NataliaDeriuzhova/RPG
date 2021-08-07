from enums.item_enums import CreatureTypes, IncreasePower


class Creature:
    def __init__(self, hp=50, creature_type=CreatureTypes.MAG.value, power=10):
        self.hp = hp
        self.creature_type = creature_type
        self.power = power

    @property
    def creature_power(self):
        _creature_power = self.power
        if self.creature_type == CreatureTypes.MAG.value:
            _creature_power = self.power * IncreasePower.MAG.value
        elif self.creature_type == CreatureTypes.ARCHER.value:
            _creature_power = self.power * IncreasePower.ARCHER.value
        return _creature_power
