import os
import pandas as pd
from .enum_classes import Element, Race, AttackType, CombatStyle
from ..directories import project_directory
from ..utils.utils import string_to_dict

DEFAULT_STAT_FILE = os.path.join( project_directory, "resources", "DefaultStats.csv" )

class Stats:
    def __init__(self, file=None, use_default=False, **kwargs):
        # Create the dictionary
        self.levels = {}

        if not file is None:
            self.setup_stats(file=file)
        elif use_default:
            self.load_defaults()
        else:
            self.load_from_kwargs(**kwargs)

    def setup_stats(self, file=None):
        if not file is None:
            self.load_from_file(file)
            return

        # Load default values
        self.load_defaults()

    def load_defaults(self):
        # Load standard level defaults
        self.load_from_file(DEFAULT_STAT_FILE)

        # Set resistances and bonuses
        for element in Element:
            self.levels[ "{} Resistance".format(element.value) ] = 0
            self.levels[ "{} Bonus".format(element.value) ] = 0
        for race in Race:
            self.levels[ "{} Resistance".format(race.value) ] = 0
            self.levels[ "{} Bonus".format(race.value) ] = 0
        for attack_type in AttackType:
            self.levels[ "{} Resistance".format(attack_type.value) ] = 0
            self.levels[ "{} Bonus".format(attack_type.value) ] = 0
        for style in CombatStyle:
            self.levels[ "{} Resistance".format(style.value) ] = 0
            self.levels[ "{} Bonus".format(style.value) ] = 0

    def load_from_file(self, file):
        data = pd.read_csv(file, sep=",")

        names = data["Name"]
        values = data["Level"]

        for i in range(len(names)):
            self.levels[names[i]] = values[i]
    
    def load_from_kwargs(self, **kwargs):
        for label in kwargs:
            self.levels[label] = kwargs[label]

    def get_stat(self, label):
        if label in self.levels:
            return self.levels[label]
        return 0

    def stats_from_string(value):
        values = string_to_dict(value, str, int)
        return Stats(**values)
    
    def __add__(self, other):
        copied = Stats( **self.levels )

        for label in other.levels:
            if label in copied.levels:
                copied.levels[label] += other.levels[label]
            else:
                copied.levels[label] = other.levels[label]
        
        return copied
