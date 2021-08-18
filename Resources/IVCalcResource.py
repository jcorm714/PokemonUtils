"""The resource for calculating IVS for a given pokemon"""
from Objects.Pokemon import Pokemon
from Objects.Nature import Nature
from Objects.Stats import Stats
from Core.scraper import BulbapediaScraper, GEN_LIST
from resource import Resource
from response import ResponseStatus, Response

class IVCalcResource(Resource):
        def __init__(self, request) -> None:
            super().__init__(request)
            self.response = Response()
        
        def process(self):
                #set pokemon values to data in the json file
                content = self.request.json()
                pokemon = Pokemon()
                pokemon.name = content["name"]
                pokemon.level = content["level"]
                nature_name  = content["nature"]
                nature = Nature(nature_name.capitalize())
                pokemon.nature = nature

                #set the pokemon's stat values 
                stat_values = content["stat_values"]
                pokemon.set_stat_totals(stat_values["atk"],
                                        stat_values["def"],
                                        stat_values["sp_atk"],
                                        stat_values["sp_def"],
                                        stat_values["spe"],
                                        stat_values["hp"])

                evs = content["evs"]
                pokemon.set_evs(evs["atk"],
                                evs["def"],
                                evs["sp_atk"],
                                evs["sp_def"],
                                evs["spe"],
                                evs["hp"])

                scraper = BulbapediaScraper()
                page = scraper.get_pokemon_page(pokemon.name)
                base_stats = scraper.get_pokemon_base_stats(page)
                
                most_recent_gen = None
                gen_list_reversed = GEN_LIST[::-1]
                for gen in gen_list_reversed:
                        if(gen in base_stats):
                                most_recent_gen = base_stats[gen]
                                break

                pokemon.set_base_stats(
                        most_recent_gen[Stats.ATTACK],
                        most_recent_gen[Stats.DEFENSE],
                        most_recent_gen[Stats.SP_ATTACK],
                        most_recent_gen[Stats.SP_DEFENSE],
                        most_recent_gen[Stats.SPEED],
                        most_recent_gen[Stats.HP])

                pokemon.calc_ivs_gen3()
                ivs = pokemon.ivs
                json_ivs = {}
                for key, value in ivs.items():
                        json_ivs[key.name.lower()] = value

