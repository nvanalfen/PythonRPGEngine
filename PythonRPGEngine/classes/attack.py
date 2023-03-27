from .enum_classes import TargetType, Element
from .requirement import Requirement
from .buff import Buff
from .damage import Damage
from ..utils.utils import string_to_dict, string_to_list, string_to_tuple

class Attack:
    def __init__ (self, name:str="", id:str="AT000", description:str="", costs:dict[str,int]={},
                  target:TargetType=TargetType.ENEMY, target_count:int=0,
                  damage:Damage=Damage(), base_accuracy:float=1, attack_range:float=1, charge_time:int=0,
                  elements:list[tuple[Element,float]]=[(Element.PHYSICAL,1)], buffs:list[str]=[],
                  requirements:Requirement=None):
        
        # Information variables
        self.name = name                            # Name of attack
        self.id = id                                # Attack id
        self.description = description              # Description of attack

        # Combat variables
        self.costs = costs                          # Cost to use. Dict from gauge (health, mana, energy, etc.) to amount needed
        self.target = target                        # Target type for the attack
        self.target_count = target_count            # Number of targets. 0 means all
                                                    # (e.g. target_type == party, target_count = 0 means target all party members)
        self.damage = damage                        # Damage object containing all the scaling and recoil information
        self.base_accuracy = base_accuracy          # Accuracy of attack before scaling
        self.attack_range = attack_range            # Range of attack (experimental)
        self.charge_time = charge_time              # Number of turns to charge/cast attack
        self.element = elements                     # List of elements attributed to attack (typically only one)
                                                    # Each element of the list is a tuple of the element and how much it affects the scaling
        self.buffs = buffs                          # list of buff id values for buffs that may apply to target

        # Requirements to use
        self.requirements = requirements            # Requirements to use attack
    
    def attack_from_string_components(name, id, description, costs, 
                                      target, target_count,
                                      damage_components,
                                      base_accuracy, attack_range, charge_time,
                                      elements, buffs,
                                      requirements_components):
        # All of the components are strings, convert non-string versions into the expected dtype
        costs = string_to_dict(costs, str, int)
        target = TargetType.get_type(target)
        target_count = int(target_count)
        damage = Damage.damage_from_string_components(*damage_components)
        base_accuracy = float(base_accuracy)
        attack_range = float(attack_range)
        charge_time = int(charge_time)
        elements = [ string_to_tuple( el, [Element.get_type, float] ) for el in string_to_list(elements) ]
        buffs = string_to_list( buffs )
        requirements = Requirement.requirement_from_string_components(*requirements_components)

        return Attack( name=name, id=id, description=description, costs=costs, target=target, target_count=target_count,
                      damage=damage, base_accuracy=base_accuracy, attack_range=attack_range, charge_time=charge_time,
                       elements=elements, buffs=buffs, requirements=requirements )