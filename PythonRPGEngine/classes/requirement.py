from .stats import Stats
from .enum_classes import WeaponType, Race
from ..utils.utils import string_to_list

class Requirement:
    def __init__(self, stats:Stats=None, level:int=1, skills:list[str]=[], equipment:list[str]=[], 
                 race:list[Race]=[], weapon_type:list[WeaponType]=[]):
        self.stats = stats                  # Stat levels required
        self.level = level                  # Overall level required

        # ID requirements
        self.skills = skills                # Skill(s) required (list of skill ids)
        self.equipment = equipment          # Equipment required (list of equipment ids)

        # Enum requirements
        self.race = race                    # Race(s) required (list of races)
        self.weapon_type = weapon_type      # Weapon Type(s) required (list of WeaponType enums)
    
    def satisfied(self, stats:Stats, level:int, skills:list[str], equipment:list[str], race:list[Race], weapon_type:list[WeaponType]):
        # Assure that everything passed satisfies requirements
        # All levels must be greater than or equal to the requirement levels
        # All ids and enums required must be included

        # Check levels
        if not stats is None:
            for label in self.stats.levels:
                if stats.levels[label] < self.stats.levels[label]:
                    return False            # If the passed in stats are lower, it is not satisfied
        if level < self.level:
            return False
        
        # Check ids
        for el in self.skills:
            if not el in skills:
                return False
        for el in self.equipment:
            if not el in equipment:
                return False
        
        # Check enums
        for el in self.race:
            if not el in race:
                return False
        for el in self.weapon_type:
            if not el in weapon_type:
                return False
        
        # If nothing failed, requirements are satisfied
        return True
    
    def requirement_from_string_components(stats, level, skills, equipment, race, weapon_type):
        stats = Stats.stats_from_string(stats)
        level = int(level)
        skills = string_to_list(skills)
        equipment = string_to_list(equipment)
        race = string_to_list(race, Race.get_type)
        weapon_type = string_to_list(weapon_type, WeaponType.get_type)

        return Requirement(stats=stats, level=level, skills=skills, equipment=equipment, race=race, weapon_type=weapon_type)