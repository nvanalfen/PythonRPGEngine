from .enum_classes import EquipmentType
from .stats import Stats
from.item import Equipment, Weapon

class Backpack:
    def __init__(self):
        self.consumables = {}
        self.armor = {}
        self.weapons = {}
        self.key_items = {}

class Outfit:
    def __init__(self, **kwargs):
        self.equipped = {}
        self.types = {}
        self.load_empty()
        self.load_from_kwargs( **kwargs )

    def load_empty(self):

        self.equipped["head"] = None
        self.equipped["neck"] = None
        self.equipped["chest"] = None
        self.equipped["back"] = None
        self.equipped["arms"] = None
        self.equipped["wrist"] = None
        self.equipped["belt"] = None
        self.equipped["legs"] = None
        self.equipped["feet"] = None
        self.equipped["hands"] = None
        self.equipped["on_hand"] = None
        self.equipped["off_hand"] = None
        self.equipped["finger_1"] = None
        self.equipped["finger_2"] = None
        self.equipped["finger_3"] = None
        self.equipped["ammo"] = None

        self.types["head"] = EquipmentType.HEAD
        self.types["neck"] = EquipmentType.NECK
        self.types["chest"] = EquipmentType.CHEST
        self.types["back"] = EquipmentType.BACK
        self.types["arms"] = EquipmentType.ARM
        self.types["wrist"] = EquipmentType.WRIST
        self.types["belt"] = EquipmentType.BELT
        self.types["legs"] = EquipmentType.LEG
        self.types["feet"] = EquipmentType.FOOT
        self.types["hands"] = EquipmentType.HAND
        self.types["on_hand"] = EquipmentType.WEAPON
        self.types["off_hand"] = EquipmentType.SHIELD               # Dual wielding skill should let this be overwritten with weapon as well
        self.types["finger_1"] = EquipmentType.FINGER
        self.types["finger_2"] = EquipmentType.FINGER
        self.types["finger_3"] = EquipmentType.FINGER
        self.types["ammo"] = EquipmentType.AMMO

    # Only load kwargs already set from load_empty
    def load_from_kwargs(self, **kwargs):
        for piece in kwargs:
            self.equip( kwargs[piece], piece )

    def equip(self, equipment:Equipment, slot:str):
        
        # Add a piece of logic to allow having a weapon in the off hand
        # This will also require another parameter to be passed in
        if equipment.piece == self.types[slot]:
            swapped = self.unequip( slot )
            self.equipped[ slot ] = equipment
            return swapped                                          # Return any equipment that was swapped
        
        # If the slot type is mismatched, return the piece of equipment passed in
        return equipment
    
    def unequip(self, slot:str):
        if slot is None or not slot in self.equipped:
            return None

        removed = self.equipped[slot]
        self.equipped[slot] = None
        return removed

    def get_stats(self):
        stats = Stats()

        for piece in self.equipped:
            if not self.equipped[piece] is None:
                stats += self.equipped[piece].stats
        
        return stats