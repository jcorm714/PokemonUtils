from flask import Flask, request, jsonify
from  flask_cors import CORS
from Pokemon import Pokemon
from scraper import BulbapediaScraper
from scraper import GEN_LIST
from Stats import Stats
from Nature import Nature

app = Flask(__name__)
CORS(app)
@app.route("/calcIV", methods=["Post"])
def calc_ivs():
        content = request.json
        
        #set pokemon values to data in the json file
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
        return jsonify(json_ivs)


