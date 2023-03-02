from enum import Enum

class Element(Enum):
    FIRE = "Fire"
    WATER = "Water"
    EARTH = "Earth"
    AIR = "Air"
    LIGHT = "Light"
    DARKNESS = "Darkness"

class Race(Enum):
    HUMAN = "Human"
    ELF = "Elf"
    DWARF = "Dwarf"
    GOBLIN = "Goblin"
    DEMON = "Demon"
    DRACONIC = "Draconic"
    BEAST = "Beast"
    MAGICAL_BEAST = "Magical Beast"

class CombatStyle(Enum):
    MELEE = "Melee"
    RANGED = "Ranged"
    MAGIC = "Magic"

class AttackType(Enum):
    NORMAL = "Normal"
    SLASHING = "Slashing"
    PIERCING = "Piercing"
    STABBING = "Stabbing"
    CRUSHING = "Crushing"