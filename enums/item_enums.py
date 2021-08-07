from enum import Enum


class ItemsEnum(Enum):
    APPLE = 'apple'
    SWORD = 'sword'
    BOOK = 'magician_book'


class CreatureTypes(Enum):
    MAG = "mag"
    ARCHER = 'archer'
    KNIGHT = 'knight'


class IncreasePower(Enum):
    MAG = 2
    ARCHER = 5
