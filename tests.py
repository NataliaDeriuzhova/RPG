import pytest
from hamcrest import assert_that, equal_to

from creature import Creature
from enums.item_enums import CreatureTypes, IncreasePower
from enums.result_enums import ResultEnum
from main import game_progress


@pytest.mark.parametrize("creature_type, power, creature_power",
                         ([CreatureTypes.KNIGHT.value, 10, 10],
                          [CreatureTypes.ARCHER.value, 16, 16 * IncreasePower.ARCHER.value],
                          [CreatureTypes.MAG.value, 90, 90 * IncreasePower.MAG.value]))
def test_creating_creature(creature_type, power, creature_power):
    knight = Creature(hp=10, creature_type=creature_type, power=power)
    assert_that(knight.creature_power, equal_to(creature_power),
                f"сила {creature_type} равна {creature_power}")


def test_knight_died():
    knight = Creature(hp=10, creature_type=IncreasePower.MAG.value, power=1)
    result = game_progress(knight)
    assert_that(result, equal_to(ResultEnum.LOOSER.value), "рыцарь проиграл")
