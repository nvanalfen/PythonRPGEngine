from .stats import Stats

class Requirement:
    def __init__(self):
        self.stats = Stats()            # Stat levels required
        self.level = 1                  # Overall level required

        # ID requirements
        self.skills = []                # Skill(s) required (list of skill ids)
        self.equipment = []             # Equipment required (list of equipment ids)

        # Enum requirements
        self.race = []                  # Race(s) required (list of races)
        self.weapon_type = []           # Weapon Type(s) required (list of WeaponType enums)
    
    def satisfied(self, stats, level, skills, equipment, race, weapon_type):
        # Assure that everything passed satisfies requirements
        # All levels must be greater than or equal to the requirement levels
        # All ids and enums required must be included

        # Check levels
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