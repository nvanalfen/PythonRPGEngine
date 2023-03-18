from .enum_classes import Element, CombatStyle, AttackType, BuffType
from .damage import Damage
from .character import Character
from .stats import Stats

class Buff:
    def __init__ (self, name:str="", buff_id:str="", duration:int=0, element:Element=Element.PHYSICAL,
                  latch:tuple[float,float]=(0,1), clearable:bool=True, stackable:bool=False, origin:Character=None,
                  buff_type:BuffType=BuffType.GENERAL):
        
        self.name = name                            # Name of buff
        self.id = buff_id                           # ID used to identify buff
        self.duration = duration                    # Max number of turns buff will last
        self.element = element                      # Element of buff
        self.latch = latch                          # Tuple of two floats giving a range in [0,1]. This is the chance the buff latches on the target
        self.clearable = clearable                  # Whether or not the buff can be cleared
        self.stackable = stackable                  # Whether or not the buff can stack
        self.origin = origin                        # Character that applied the buff

        self.buff_type = buff_type                  # Type of buff. Which subclass. Used for organization

    def buff_from_string_components():
        pass

class DOTBuff(Buff):
    def __init__ (self, name:str="", buff_id:str="", duration:int=0, element:Element=Element.PHYSICAL,
                  latch:tuple[float,float]=(0,1), clearable:bool=True, stackable:bool=False, origin:Character=None,
                  damage:Damage=None, ignore_armor:bool=False, ignore_shield:bool=False, ignore_defense:bool=False,
                  combat_style:CombatStyle=CombatStyle.MELEE, attack_type:AttackType=AttackType.NORMAL):
        
        super().__init__(self, name=name, buff_if=buff_id, duration=duration, element=element, latch=latch, 
                         clearable=clearable, stackable=stackable, origin=origin, buff_type=BuffType.DOT)
        
        self.damage = damage                        # Damage object for how the damage will be applied
        self.ignore_armor = ignore_armor            # Whether to account for armor when damage is being applied
        self.ignore_shield = ignore_shield          # Whether to account for shields when damage is applied
        self.ignore_defense = ignore_defense        # Whether to account for defense level when damage is applied
        self.combat_style = combat_style            # What type of damage (melee, magic, ranged, etc)
        self.attack_type = attack_type              # What type of strike (slashing, crushing, etc.)

# Similar to DOT buff in some ways, but simpler
# This allows draining or regenerating without first damaging abother (drain in Damage must cause damage to drain)
# A RegenBuff with negative health amount could be used similar to a True Damage DOT
class RegenBuff(Buff):
    def __init__(self, name:str="", buff_id:str="", duration:int=0, element:Element=Element.PHYSICAL,
                  latch:tuple[float,float]=(0,1), clearable:bool=True, stackable:bool=False, origin:Character=None,
                  amount:tuple[int,int]=(1,1), gauge:str="health", absolute:bool=True):
        
        super().__init__(self, name=name, buff_if=buff_id, duration=duration, element=element, latch=latch, 
                         clearable=clearable, stackable=stackable, origin=origin, buff_type=BuffType.REGEN)
        
        self.amount = amount                        # Range to randomly draw regeneration amount from
        self.gauge = gauge                          # Which gauge to regenerate or drain (health, mana, energy, etc)
        self.absolute = absolute                    # Whether the amount regenerated/depleted is absolute (value drawn),
                                                    # or relative (proportion of max)

class ShieldBuff(Buff):
    def __init__ (self, name:str="", buff_id:str="", duration:int=0, element:Element=Element.PHYSICAL,
                  latch:tuple[float,float]=(0,1), clearable:bool=True, stackable:bool=False, origin:Character=None,
                  amount:int=0, resistances:Stats=None):
        
        super().__init__(self, name=name, buff_if=buff_id, duration=duration, element=element, latch=latch, 
                         clearable=clearable, stackable=stackable, origin=origin, buff_type=BuffType.SHIELD)
        
        self.amount = amount                        # Total amount the shield can block
        self.resistances = resistances              # Stats object to give the resistances of the shield. Used for gauging how much damage will be done

class StatsBuff(Buff):
    def __init__ (self, name:str="", buff_id:str="", duration:int=0, element:Element=Element.PHYSICAL,
                  latch:tuple[float,float]=(0,1), clearable:bool=True, stackable:bool=False, origin:Character=None,
                  stats:Stats=None, absolute:bool=True):
        
        super().__init__(self, name=name, buff_if=buff_id, duration=duration, element=element, latch=latch, 
                         clearable=clearable, stackable=stackable, origin=origin, buff_type=BuffType.STATS)
        
        self.stats = stats                          # Stats object giving stat boosts
        self.absolute = absolute                    # Whether the boosts are absolute (True), or a proportion of base stats (False)