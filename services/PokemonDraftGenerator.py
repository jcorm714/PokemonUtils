from .Service import Service
from time import sleep
import pokebase as pkb
import pandas as pd
import logging
import os.path
from io import StringIO
logging.basicConfig(format="[%(asctime)s %(levelname)s %(filename)s]: %(message)s", filename="app.log")

class PokemonDraftGenerator(Service):

        def __init__(self) -> None:
                super().__init__()
                self.pokemon_entries = []
                self.pokemon_entries_df = None
                self.active_dex_id = None
                self.active_dex_name= None
                self.output = None
        def process_request(self):
                self.determine_active_dex()
                if not os.path.exists(self.get_cache_dex_uri()):
                        self.get_pokemon_for_dex()
                else:
                      pokemon_entries_df =  pd.read_csv(self.get_cache_dex_uri())
                self.make_draft_csv()
        
        def get_cache_dex_uri(self):
                return f"cache/{self.service_options.region}_dex.csv"

        def determine_active_dex(self):
                dexes = list(pkb.APIResourceList("pokedex"))
                region = self.service_options.region
                for dex in dexes:
                        if region == dex["name"]:
                                #get the last character before the final '/'
                                dex_num = dex["url"][-2]
                                self.active_dex_id = int(dex_num)
                                self.active_dex_name = dex["name"]
                                return
                raise ValueError(f"No region found for '{region}'")

        def get_pokemon_for_dex(self):
                pokemon_list = pkb.APIResource("pokedex", self.active_dex_id)
                for pokemon in pokemon_list.pokemon_entries:
                        try:
                                pk_species = pokemon.pokemon_species
                                poke = dict()
                                poke["name"] = pk_species.name
                                poke["is_baby"] = pk_species.is_baby
                                poke["is_legendary"] = pk_species.is_legendary
                                poke["is_mythical"] = pk_species.is_mythical
                                if(not (pk_species.is_baby and 
                                        pk_species.is_legendary and 
                                        pk_species.is_mythical)):
                                                poke["is_pokemon"] = True
                                print("appending " + pk_species.name)
                                self.pokemon_entries.append(poke)
                                sleep(0.7)
                        except Exception as e:
                                logging.error(e)
                                sleep(10)

                self.pokemon_entries_df= pd.DataFrame(self.pokemon_entries)
                self.pokemon_entries_df.to_csv(self.get_cache_dex_uri(), index=False)

        def make_draft_csv(self):
                if self.pokemon_entries_df is None:
                        self.pokemon_entries_df = pd.read_csv(self.get_cache_dex_uri())

                exclude_filters = []
                if self.service_options.exclude:
                        exclude_filters = self.service_options.exclude.split(",")


                def __classify_row(row):
                        if(row["is_baby"]):
                                return "BABY"
                        if(row["is_legendary"]):
                                return "LEGENDARY"
                        if(row["is_mythical"]):
                                return "MYTHICAL"
                        if(row["is_pokemon"]):
                                return "POKEMON"

                self.pokemon_entries_df["pokemon_category"] = self.pokemon_entries_df.apply (lambda row: __classify_row(row), axis=1)
                bools = ~self.pokemon_entries_df["pokemon_category"].isin(exclude_filters)
                filtered = self.pokemon_entries_df[bools]
                filterted_no_bool_cols = filtered[["name", "pokemon_category"]]
                sample = filterted_no_bool_cols.sample(self.service_options.sample_size, replace=self.service_options.replace_when_sample)
                self.service_output = StringIO()
                sample.to_csv(self.service_output, index=False)



        
   
                        
                
                        
                        

