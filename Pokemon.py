"""This Class represents a Pokemon and its data"""

from enum import Enum
from Nature import Nature
from Nature import get_affected_stats

class Stats(Enum):
        """An enum representing each pokemon stat"""
        ATTACK = "Attack"
        DEFENSE = "Defense"
        SP_ATTACK = "Special_Attack"
        SP_DEFENSE = "Special_Defense"
        SPEED = "Speed"

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
                        the nature the pokemon has """
        def __init__(self) -> None:
            self.name = ""
            self.evs = {
                    Stats.ATTACK: 0,
                    Stats.DEFENSE: 0,
                    Stats.SP_ATTACK: 0,
                    Stats.SP_DEFENSE: 0,
                    Stats.SPEED: 0,
            }
            self.ivs = {
                    Stats.ATTACK: 0,
                    Stats.DEFENSE: 0,
                    Stats.SP_ATTACK: 0,
                    Stats.SP_DEFENSE: 0,
                    Stats.SPEED: 0,
            }
            self.base_stats = {
                    Stats.ATTACK: 0,
                    Stats.DEFENSE: 0,
                    Stats.SP_ATTACK: 0,
                    Stats.SP_DEFENSE: 0,
                    Stats.SPEED: 0,
            }
            self.nature = Nature.HASTY