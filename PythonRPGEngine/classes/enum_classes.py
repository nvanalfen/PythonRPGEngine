from enum import Enum

class Element(Enum):
    PHYSICAL = "Physical"
    FIRE = "Fire"
    WATER = "Water"
    EARTH = "Earth"
    AIR = "Air"
    LIGHT = "Light"
    DARKNESS = "Darkness"
    POISON = "Poison"

    def get_type(text):
        for element in Element:
            if element.value == text:
                return element

class Race(Enum):
    HUMAN = "Human"
    ELF = "Elf"
    DWARF = "Dwarf"
    GOBLIN = "Goblin"
    DEMON = "Demon"
    DRACONIC = "Draconic"
    BEAST = "Beast"
    MAGICAL_BEAST = "Magical Beast"
    UNDEAD = "Undead"

    def get_type(text):
        for race in Race:
            if race.value == text:
                return race

class CombatStyle(Enum):
    MELEE = "Melee"
    RANGED = "Ranged"
    MAGIC = "Magic"

    def get_type(text):
        for style in CombatStyle:
            if style.value == text:
                return style

class AttackType(Enum):
    NORMAL = "Normal"
    SLASHING = "Slashing"
    PIERCING = "Piercing"
    STABBING = "Stabbing"
    CRUSHING = "Crushing"

    def get_type(text):
        for style in AttackType:
            if style.value == text:
                return style

class WeaponType(Enum):
    SWORD = "Sword"
    GREATSWORD = "Greatsword"
    DAGGER = "Dagger"
    WARHAMMER = "Warhammer"
    BATTLEAXE = "Battleaxe"
    POLEARM = "Polearm"
    STAFF = "Staff"
    BOW = "Bow"
    CATALYST = "Catalyst"

    def get_type(text):
        for weapon in WeaponType:
            if weapon.value == text:
                return weapon

class EquipmentType(Enum):
    WEAPON = "Weapon"
    SHIELD = "Shield"
    HEAD = "Head"
    CHEST = "Chest"
    LEG = "Leg"
    FOOT = "Foot"
    HAND = "Hand"
    BELT = "Belt"
    FINGER = "Finger"
    WRIST = "Wrist"
    NECK = "Neck"
    BACK = "Back"
    AMMO = "Ammo"

    def get_type(text):
        for eq in EquipmentType:
            if eq.value == text:
                return eq
            
class TargetType(Enum):
    SELF = "Self"                   # Character
    PARTY = "Party"                 # Some number >= 1 of party (character included)
    ALL_PARTY = "All Party"         # The whole party (character included)
    ALLY = "Ally"                   # Some number >= 1 of allies (character excluded)
    ALL_ALLY = "All Ally"           # All allies (character excluded)
    ENEMY = "Enemy"                 # Some number >= 1 of enemies
    ALL_ENEMY = "All Enemy"         # All enemies

    def get_type(text):
        for target in TargetType:
            if target.value == text:
                return target