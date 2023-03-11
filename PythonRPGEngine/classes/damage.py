from ..utils.utils import string_to_list, string_to_tuple, string_to_dict

class Damage:
    def __init__ (self, base_damage:float=1., scalings:dict[str,float]={"Attack":1}, recoil:tuple[float,float]=(0,0),
                  target_gauges:dict[str,tuple[float,float]]={"health":(0.,1.)}, absolute_damage:bool=True,
                  drains:dict[tuple[str,str],tuple[float,float]]={}):
        """
        Parameters
        ----------
        base_damage : float
                    Damage of attack before scaling has been applied
        scalings : dict[ str, float ]
                    Dict of scalings where each key,value pair is a scaling.
                    A scaling is the level the damage will scale on (key) and the proportion it will scale by (value).
                    The scaling follows base_attack * sum{ level * scaling_amount }
                    e.g. a base damage of 1 with an attack scaling of 1.5 with an attack level of 2 would yield a result of 1*(1.5 * 2)
                    With multiple scalings, add them all.
                    e.g. a base_damage of 1, and attack and defense scalings of 1.5 and 2.5 respectively with levels of 3 and 4 respectively would be
                    1 * ( (1.5*2) + (2.5*4) )
        recoil : tuple(float, float)
                    The proportion of damage inflicted to rebound on the attacker. The tuple indicates a lower and upper range of proportions
                    to be randomly drawn and applied.
                    Equivalent to a drain of ("health", "health") : recoil in drains below.
                    Since this is a more common case, it has its own variable, even though it can be accounted for by another mechanic.
                    This value will be added into drains rather than kept as its own variable.
        target_gauges : dict{ str : tuple(float, float) }
                    List of target relationships. Each target is a tuple of a string and a second tuple of two floats
                    Rather than only attacking health, target_gauges allows the damage calculated to deduct form any gauge (health, mana, etc.)
                    The first element of each relationship is the gauge to attack.
                    The second element is a tuple that indicates the range for a random draw for the final value
                    e.g. for a scaled value above of 5, and a target_gauge of ("health", (0.5,1)), the random draw would pick a number
                    between 0.5 and 1 and multiply that by the scaled value above.
        absolute_damage : bool, default is True
                    Whether to treat the damage calculated as the absolute amount of damage (value of True), or a proportion of the target's
                    health (or mana, energy, etc.) (value of False)
        drains : dict{ tuple(str, str) : tuple(float, float) }
                    "Recoil"-like values to apply to the attacker. Whatever damage or drain is done to the target, some proportion will rebound
                    onto the attacker.
                    The key of the dict is a tuple of (str, str). The first string is the gauge being targeted (e.g. opponent's health) and
                    the second string is the gauge to be affected in the attacker (e.g. attacker's mana).
                    The value of the dict is a float range for a random draw to determine a proportion of the damage done to the target's
                    gauge to be applied to the attacker's gauge.
                    e.g. { ("health","mana") : (-0.5, 0) } would indicate a random number to be drawn between -0.5, and 0.
                    If the random number is -0.25, this indicates that the attacker "gains" -0.25*(damage done to target's health).
                    The negative indicates this is a loss to the attacker. So if the attack dealt 5 damage, the attacker would lose 0.25*5 mana

        """
        
        self.base_damage = base_damage                      # Base damage of attack before scaling
        self.scalings = scalings                            # Scaling parameters. list of tuples where each tuple is a scaling
                                                            # A scaling is the level it scales on and what proportion of the level it scales by
                                                            # e.g. a base damage of 1 with an attack scaling of 1.5 and an attack level of 2
                                                            # would yield a result of base_damage * (attack_level*scaling) = 1 * (1.5*2)
                                                            # With multiple scalings, add them all
        self.absolute_damage = absolute_damage
        self.target_gauges = target_gauges
        self.drains = drains
        self.drains[("health","health")] = recoil
    
    def damage_from_string_components(base_damage, scalings, recoil, target_gauges, absolute_damage, drains):
        base_damage = float(base_damage)
        scalings = string_to_dict( scalings, str, float )
        recoil = string_to_tuple( recoil, [float, float] )
        target_gauges = { key : string_to_tuple(value, [float, float]) 
                         for key, value in string_to_dict(target_gauges, str, str, dict_sep=",,").items() }
        absolute_damage = ( absolute_damage.strip().lower() == "true" ) or ( absolute_damage.strip().lower() == "1" )
        drains = { string_to_tuple( key, [str, str] ) : string_to_tuple( value, [float, float] ) 
                  for key,value in string_to_dict(drains, str, str, dict_sep=",,").items() }

        return Damage(base_damage=base_damage, scalings=scalings, recoil=recoil, target_gauges=target_gauges, 
                      absolute_damage=absolute_damage, drains=drains)