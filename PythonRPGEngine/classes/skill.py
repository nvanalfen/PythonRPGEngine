from .requirement import Requirement
from .buff import Buff
from .stats import Stats
from ..utils.utils import string_to_list

class Skill:
    def __init__ (self, name:str="", skill_id:str="SK000", description:str="",
                  requirements:Requirement=None, boons:list[str]=[], stats:Stats=None):
        self.name = name                            # Name of skill
        self.id = skill_id                          # ID of skill
        self.description = description              # Description of skill
        self.requirements = requirements            # Requirements for skill
        self.boons = boons                          # List of buff ids given by skill
        self.stats = stats                          # Level stat bonuses given by skill
    
    def skill_from_string_components(name, skill_id, description, requirement_components, boons, stats):
        requirements = Requirement.requirement_from_string_components(*requirement_components)
        boons = string_to_list(boons)
        stats = Stats.stats_from_string(stats)

        return Skill(name=name, skill_id=skill_id, description=description, requirements=requirements, boons=boons, stats=stats)