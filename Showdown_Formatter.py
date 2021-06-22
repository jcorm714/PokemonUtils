from Pokemon import Pokemon
from Stats import Stats
import typing

class Showdown_Formatter:
        StatNameMap = {
                Stats.HP: "HP",
                Stats.ATTACK: "Atk",
                Stats.DEFENSE: "Def",
                Stats.SP_ATTACK: "SpA",
                Stats.SP_DEFENSE: "SpD",
                Stats.SPEED: "Spe"
        }
        def __init__(self, pokemon:Pokemon) -> None:
            self.pokemon = pokemon
        

        def format(self) -> str:
                formatString = ""
                formatString += f"{self.pokemon.name} \n"
                formatString += f"Level: {self.pokemon.level} \n" 
                
                #evs
                formatString += "EVs: "
                for key in self.pokemon.evs.keys():
                        if(self.pokemon.evs[key] > 0):
                                formatString += f"{self.pokemon.evs[key]} {Showdown_Formatter.StatNameMap[key]} /"
                
                #remove last '/' character
                formatString = formatString[0:len(formatString) -1]
                formatString += '\n'

                formatString += f"{self.pokemon.nature.name} Nature \n"
                
                formatString += "IVs: "
                for key in self.pokemon.ivs.keys():
                        if(self.pokemon.ivs[key] > 0):
                                formatString += f"{self.pokemon.ivs[key]} {Showdown_Formatter.StatNameMap[key]} /"
                
                formatString = formatString[0:len(formatString) -1]
                formatString += '\n'

                return formatString
                


