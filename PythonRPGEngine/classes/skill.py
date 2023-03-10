from .requirement import Requirement
from .buff import Buff
from .stats import Stats

class Skill:
    def __init__ (self, name="", skill_id=-1, description=""):
        self.name = name                            # Name of skill
        self.id = skill_id                          # ID of skill
        self.description = description              # Description of skill
        self.requirements = Requirement()           # Requirements for skill
        self.boons = []                             # List of Buff objects given by skill
        self.boosts = Stats()                       # Level bonuses given by skill