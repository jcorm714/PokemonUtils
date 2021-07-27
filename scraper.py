"""This file contains scripts for a webscrapper that finds various sections
on bulbapedia"""

import requests
import logging
from Stats import Stats
from bs4 import BeautifulSoup, SoupStrainer

logging.basicConfig(format="[%(asctime)s %(levelname)s]: %(message)s", level=logging.DEBUG)

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

        def get_pokemon_base_stats(self, pokemon_page):
                """looks for the pokemon's base stats inside the page returns a dictionary
                with keys of Stats.py
                Parameters
                ----------
                        pokemon_page str html of the webpage"""
                base_stats={}
                if(pokemon_page is None):
                        logging.warning("Invalide page data for pokemon")
                        return
                
                def parse_base_stats_table(tbl_markup): 
                        stats = {}
                        headers = tbl_markup.find_all("th")
                        for header in headers:
                                pass
                        return stats


                parser = BeautifulSoup(pokemon_page, "html.parser")
                base_stats_section = parser.find("h4", id="Base_stats")
                base_stats_title = base_stats_section.next_sibling
                if("Generation" in base_stats_title):
                        table = base_stats_title.next_sibling
                        parse_base_stats_table(table)
                
                print(base_stats)


if(__name__ == "__main__"):
        scraper = BulbapediaScraper()
        page = scraper.get_pokemon_page("pikachu")
        scraper.get_pokemon_base_stats(page)




