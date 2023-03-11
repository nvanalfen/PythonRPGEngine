from .stats import Stats
from .enum_classes import EquipmentType, WeaponType
from .requirement import Requirement
from .buff import Buff
from .attack import Attack

class Item:
    def __init__ (self, name:str="", id:str="IT000", description:str="", cost:int=0, rarity:int=0):
        self.name = name
        self.item_id = id
        self.description = description
        self.base_cost = cost
        self.rarity = rarity

class Consumable(Item):
    def __init__ (self, name:str="", id:str="CON000", description:str="", cost:int=0, rarity:int=0, 
                  regen:dict={}, boons:list[Buff]=[], blights:list[Buff]=[]):
        
        # Call super constructor
        super().__init__(name=name, id=id, description=description, cost=cost, rarity=rarity)

        # Set specific variables
        self.regen = regen                  # Amount of gauges (health, mana, energy, etc) to recover
        self.boons = boons                  # Boons (buffs) to apply
        self.blights = blights              # Blights (debuffs) to apply

class Equipment(Item):
    def __init__ (self, name:str="", id:str="EQ000", description:str="", cost:int=0, rarity:int=0,
                  piece:EquipmentType=None, requirements:Requirement=None, stats:Stats=None,
                  attacks:list[Attack]=[], boons:list[Buff]=[], blights:list[Buff]=[]):
        
        # Call super constructor
        super().__init__(name=name, id=id, description=description, cost=cost, rarity=rarity)

        # Set specific variables
        self.piece = piece                          # EquipmentType of this piece of equipment
        self.requirements = requirements            # Requirements to use/wear this equipment
        self.stats = stats                          # Stat boosts from wearing/wielding
        self.attacks = attacks                      # Attacks granted while wearing/wielding
        self.boons = boons                          # Buffs to apply upon battle start
        self.blights = blights                      # Debuffs to apply on battle start

class Weapon(Equipment):
    def __init__ (self, name:str="", id:str="WE000", description:str="", cost:int=0, rarity:int=0,
                  piece:EquipmentType=None, requirements:Requirement=None, stats:Stats=None,
                  attacks:list[Attack]=[], boons:list[Buff]=[], blights:list[Buff]=[],
                  weapon_type:WeaponType=None, hands:int=1):
        
        # Call super constructor
        super().__init__(name=name, id=id, description=description, cost=cost, rarity=rarity,
                         piece=piece, requirements=requirements, stats=stats, attacks=attacks,
                         boons=boons, blights=blights)
        
        # Set specific variables
        self.weapon_type = weapon_type              # Weapon type
        self.hands = hands                          # Number of hands needed to wield (1=single-hand, 2=dual-hand)