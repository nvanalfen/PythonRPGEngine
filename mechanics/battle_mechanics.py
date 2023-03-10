from ..classes.enum_classes import Element, Race, AttackType, CombatStyle

# Boost calculations
def boost_element(level):
    # Linear growth for the first 10 levels
    # Slower Linear growth after that until level 50
    # Slight jump and an asymptote approaching 0.6 (60%) after that
    # Set so that level 100 gives about a 50% boost (51%)
    if level <= 10:
        return (level)/100
    elif level <= 50:
        return ( (0.5*level) + 5 )/100
    else:
        return ( level )/( level + 20 ) - 0.4

def boost_race(level):
    # I want this to be a slighter advantage. Maybe an asymptote approaching 30%
    pass

def boost_attack_type(level):
    # Asymptote of 50%?
    pass

def boost_combat_style(level):
    # 50% boost by level 100?
    pass

# Resistance calculations
def resist_element(level):
    # Ultimately have an asymptote approaching 100%
    # roughly 30% by level 50?
    pass

def resist_race(level):
    # Max resistance of 30%
    pass

def resist_attack_type(level):
    # Asymptote approaching 100%
    pass

def resist_combat_style(level):
    # Asymptote approaching 70%
    pass