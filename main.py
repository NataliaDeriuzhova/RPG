from action import Action
from creature import Creature
from enums.item_enums import CreatureTypes
from enums.result_enums import ResultEnum


def game_start():
    # приветствие - хочешь сыграть в игру?
    # Хочешь загрузить игру? (проверка если ли сохраненная игра)
    # Или Выбери персонажа
    # происходит получение сущности Creature, где hp, creature_type, power подставляются
    return Creature(hp=10, creature_type=CreatureTypes.ARCHER.value, power=6)


def game_progress(knight):
    make_action = Action()
    knight = make_action.do_action(knight)
    if knight.hp > 0:
        return game_progress(knight)
    else:
        return ResultEnum.LOOSER.value


def game():
    knight = game_start()
    game_progress(knight)


if __name__ == '__main__':
    game()
