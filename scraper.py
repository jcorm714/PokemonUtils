"""This file contains scripts for a webscrapper that finds various sections
on bulbapedia"""

import requests
import logging
import json
from Stats import Stats
from bs4 import BeautifulSoup

logging.basicConfig(format="[%(asctime)s %(levelname)s]: %(message)s", level=logging.DEBUG)

GEN_LIST = ["I", "II", "III", "IV", "V" , "VI", "VII","VIII"]

class BulbapediaScraper:
        """A class that contains methods to scrape the bulbapedia website"""
        
        def __init__(self) -> None:
            self.resp = None
            self.url = None
            self.content = None

        def get_pokemon_page(self, pokemon_name):
                """returns the pokemon's page from bulbapedia, None if the pokemon is found 
                Parameters
                ----------
                        pokemon_name: str 
                                name of the to search for"""

                
                name = pokemon_name.replace(" ", "_")
                url = rf"https://bulbapedia.bulbagarden.net/wiki/{name}_(Pokémon)"
                resp = requests.get(url)
                logging.debug(f"GET {resp.status_code} {url}")
                if(resp.status_code != 200):
                        logging.warning(f"Unable to find pokemon: {pokemon_name}")
                        return
                return resp.content


        def __parse_base_stats_table(self, tbl_markup): 
                stats = {}
                headers = tbl_markup.find_all("tr")
                #the first two rows are the title, and padding in the table
                data = headers[2:]
                for header in data:
                        divs = header.find_all("div")
                        #break when we hit the stat total row, that can be calculated
                        if(len(divs) == 2):
                                break
                        stat_name, value, _ = divs
                        value = int(value.string)
                        stat = stat_name.find("span")
                        if(stat.string == "HP"):
                                stats[Stats.HP] = value
                        elif(stat.string == "Attack"):
                                stats[Stats.ATTACK] = value
                        elif(stat.string == "Defense"):
                                stats[Stats.DEFENSE] = value
                        elif(stat.string == "Sp. Atk"):
                                stats[Stats.SP_ATTACK] = value
                        elif(stat.string == "Sp. Def"):
                                stats[Stats.SP_DEFENSE] = value
                        elif(stat.string == "Speed"):
                                stats[Stats.SPEED] = value
                return stats


        def get_pokemon_base_stats(self, pokemon_page):
                """looks for the pokemon's base stats inside the page returns a dictionary
                with keys of Stats.py
                Parameters
                ----------
                        pokemon_page html of the webpage"""
                if(pokemon_page is None):
                        logging.warning("Invalide page data for pokemon")
                        return
                
                base_stats_by_gen = {}
                parser = BeautifulSoup(pokemon_page, "html.parser")
                base_stats_section = parser.find("span", id="Base_stats")
                table_title = base_stats_section.parent.find_next("h5")
                while (table_title is not None and 
                       "Generation" in table_title.string): 

                        tbl = table_title.find_next("table")
                        stats = self.__parse_base_stats_table(tbl)
                        gen = table_title.string
                        gen = gen.replace("Generation", "");
                        gen = gen.replace("s","")
                        gen = gen.strip()
                        if("onward" in gen):
                                gen = gen.replace("onward", "")
                                gen = gen.strip()
                                start = GEN_LIST.index(gen)
                                for i in range(start, len(GEN_LIST)):
                                        base_stats_by_gen[GEN_LIST[i]] = stats
                                break;
                        elif ('-' in gen):
                                gen_start, gen_stop = gen.split("-")
                                start_idx = GEN_LIST.index(gen_start)
                                end_idx = GEN_LIST.index(gen_stop)
                                for i in range(start_idx, end_idx):
                                        base_stats_by_gen[GEN_LIST[i]] = stats
                        else:
                                base_stats_by_gen[gen] = stats
                        table_title = table_title.find_next("h5")

                
                return base_stats_by_gen


if(__name__ == "__main__"):
        scraper = BulbapediaScraper()
        page = scraper.get_pokemon_page("pikachu")
        print(scraper.get_pokemon_base_stats(page))




