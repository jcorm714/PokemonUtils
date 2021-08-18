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
        

        return jsonify(json_ivs)


