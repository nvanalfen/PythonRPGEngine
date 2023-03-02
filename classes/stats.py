import os
import pandas as pd
from .enum_classes import Element, Race, AttackType, CombatStyle
from ..directories import project_directory

DEFAULT_STAT_FILE = os.path.join( project_directory, "resources", "DefaultStats.csv" )

class Stats:
    def __init__(self, file=None):
        # Create the dictionary
        self.levels = {}

        self.setup_stats(file=file)

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

    def get_stat(self, label):
        if label in self.levels:
            return self.levels[label]
        return 0

