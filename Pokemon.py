"""This Class represents a Pokemon and its data"""

from Nature import Nature
from Nature import get_affected_stats
from Stats import Stats
class Pokemon:
        """A Class that represents all of the data pertaining to a pokemon
        Properties
        ----------
                name: str
                        the name of the pokemon
                evs: dict, Keys: Stats Enum
                        the number of EVs a pokemon has in a stat
                ivs: dict, Keys: Stats Enum
                        the number of IVs a pokemon has in each stat
                base_stats: dict, Keys: Stats Enum
                        the number of base stats a pokemon has
                nature: Nature Enum
                        the nature the pokemon has
                level: int
                        the level of the pokemon """
        def __init__(self) -> None:
            self.name = ""
            self.level = 1
            self.nature = Nature.HASTY

            self.evs = {
                    Stats.ATTACK: 0,
                    Stats.DEFENSE: 0,
                    Stats.SP_ATTACK: 0,
                    Stats.SP_DEFENSE: 0,
                    Stats.SPEED: 0,
                    Stats.HP: 0
            }
            self.ivs = {
                    Stats.ATTACK: 0,
                    Stats.DEFENSE: 0,
                    Stats.SP_ATTACK: 0,
                    Stats.SP_DEFENSE: 0,
                    Stats.SPEED: 0,
                    Stats.HP: 0
            }
            self.base_stats = {
                    Stats.ATTACK: 0,
                    Stats.DEFENSE: 0,
                    Stats.SP_ATTACK: 0,
                    Stats.SP_DEFENSE: 0,
                    Stats.SPEED: 0,
                    Stats.HP: 0
            }
            self.stat_totals = {
                    Stats.ATTACK: 0,
                    Stats.DEFENSE: 0,
                    Stats.SP_ATTACK: 0,
                    Stats.SP_DEFENSE: 0,
                    Stats.SPEED: 0,
                    Stats.HP: 0
            }


        def set_base_stats(self, atk:int, def_:int, spa:int, spd:int, spe:int, hp:int):
                """Set the base stats of a pokemon
                        atk: int
                                the base attack of a pokemon
                        def: int
                                the base defense of a pokemon
                        spa: int
                                the base special attack of a pokemon
                        spd: int
                                the base special defense of a pokemon
                        spe: int 
                                the base speed of a pokemon"""
                self.base_stats[Stats.ATTACK] = atk
                self.base_stats[Stats.DEFENSE] = def_
                self.base_stats[Stats.SP_ATTACK] = spa
                self.base_stats[Stats.SP_DEFENSE] = spd
                self.base_stats[Stats.SPEED] = spe
                self.base_stats[Stats.HP] = hp


        def set_evs(self, atk:int, def_:int, spa:int, spd:int, spe:int, hp:int):
                """Set the EVs of a pokemon
                Parameters
                ----------
                        atk: int  
                                the attack EV of a pokemon
                        def: int
                                the defense EV of a pokemon
                        spa: int
                                the special attack EV of a pokemon
                        spd: int
                                the special defense EV of a pokemon
                        spe: int 
                                the speed EV of a pokemon
                        hp: int 
                                the hp EV for a pokemon"""

                self.evs[Stats.ATTACK] = atk
                self.evs[Stats.DEFENSE] = def_
                self.evs[Stats.SP_ATTACK] = spa
                self.evs[Stats.SP_DEFENSE] = spd
                self.evs[Stats.SPEED] = spe
                self.evs[Stats.HP] = hp

        def set_stat_totals(self, atk:int, def_:int, spa:int, spd:int, spe:int, hp:int):
                """Set the current stats of your pokemon
                Parameters
                ----------
                        atk: int  
                                the attack EV of a pokemon
                        def: int
                                the defense EV of a pokemon
                        spa: int
                                the special attack EV of a pokemon
                        spd: int
                                the special defense EV of a pokemon
                        spe: int 
                                the speed EV of a pokemon
                        hp: int
                                the hp EV for a pokemon"""

                self.stat_totals[Stats.ATTACK] = atk
                self.stat_totals[Stats.DEFENSE] = def_
                self.stat_totals[Stats.SP_ATTACK] = spa
                self.stat_totals[Stats.SP_DEFENSE] = spd
                self.stat_totals[Stats.SPEED] = spe
                self.stat_totals[Stats.HP] = hp


        def calc_ivs_gen3(self):
                """Calculates the IVs for a given pokemon. The formula 
                is the same since the third generation of pokemon"""


                # see https://bulbapedia.bulbagarden.net/wiki/Individual_values
                # for more details on how to calculate IVs
                # The formula for hp is
                # hp_total =  [(2 * Base + IV + [EV/4])/100] + Level + 10
                # Rearranging the formula
                # -----------------------
                #   IV = [(Total - level - 10) * 100]/level - 2 * Base - (EV/4)

                hp_iv = (self.stat_totals[Stats.HP] - self.level - 10) * 100
                hp_iv = round(hp_iv/self.level)
                hp_iv = hp_iv - 2 * self.base_stats[Stats.HP] 
                hp_iv = hp_iv - round(self.evs[Stats.HP]/4)
                hp_iv = round(hp_iv)

                self.ivs[Stats.HP] = hp_iv
                # the formula for the other stats is
                # stat_total = [([(2 * Base + IV + [EV/4]) * level]/100) + 5] * Nature
                # the nature is a 10% modifier to two different stats
                # on of the stats is hindered while the other is helped
                # Rearranging the formula
                # -----------------------
                # IV = ((Stat/Nature - 5) * 100) / Level - 2*Base - EV/4
                self.ivs[Stats.ATTACK] = self.__calc_stat_iv(Stats.ATTACK)
                self.ivs[Stats.DEFENSE] = self.__calc_stat_iv(Stats.DEFENSE)
                self.ivs[Stats.SP_ATTACK] = self.__calc_stat_iv(Stats.SP_ATTACK)
                self.ivs[Stats.SP_DEFENSE] = self.__calc_stat_iv(Stats.SP_DEFENSE)
                self.ivs[Stats.SPEED] = self.__calc_stat_iv(Stats.SPEED)
                

        def __calc_stat_iv(self, stat:Stats) -> int:
                """Calcs the stats for others stats besides HP,
                Parameters
                ----------
                        stat: Stats Enum Note: Does not work for HP
                                the stat to calculate for
                """
                modifier = 1
                modifiers = get_affected_stats(self.nature)
                if modifiers["POS"] == stat:
                        modifier = 1.1
                elif modifiers["NEG"] == stat:
                        modifier = 0.9

                stat_iv = round(self.stat_totals[stat]/modifier) -5 
                stat_iv = stat_iv * 100
                stat_iv = round(stat_iv/self.level)
                stat_iv = stat_iv - 2 * self.base_stats[stat]
                stat_iv = stat_iv - round(self.evs[stat])/4

                # for some reason it always comes out one less when there is a nature modifier
                # so I'm adding it back here lol
                if modifier != 1:
                        stat_iv += 1
                return int(stat_iv)



