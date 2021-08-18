from Objects.Pokemon import Pokemon
from Objects.Nature import Nature
from Core.ShowdownFormatter import ShowdownFormatter
import unittest

class PokemonTests(unittest.TestCase):

        def test_pokemon_calc(self):
                poke = Pokemon()
                poke.name = "Flaaffy"
                poke.nature = Nature.TIMID
                poke.level = 45
                poke.set_base_stats(atk=55,def_=55, spa=80, spd=60,spe=45,hp=70)
                poke.set_evs(atk=48,def_=36,spa=172,spd=80,spe=76, hp=96)
                poke.set_stat_totals(atk=63,def_=67,spa=108,spd=79,spe=70,hp=140)
                poke.calc_ivs_gen3()

                formatter = ShowdownFormatter(poke)
                format = formatter.format()
                self.assertEqual(format, "Flaaffy \nLevel: 45 \nEVs: 48 Atk / 36 Def / 172 SpA / 80 SpD / 76 Spe / 96 HP \nTimid Nature \nIVs: 23 Atk / 19 Def / 26 SpA / 24 SpD / 23 Spe / 25 HP \n")

                poke2 = Pokemon()
                poke2.name = "Blissey"
                poke2.nature = Nature.SASSY
                poke2.level = 95
                poke2.set_base_stats(atk=10,def_=10, spa=75, spd=135,spe=55,hp=255)
                poke2.set_evs(atk=64,def_=0,spa=56,spd=108,spe=28, hp=252)
                poke2.set_stat_totals(atk=49,def_=36,spa=178,spd=341,spe=117,hp=676)
                poke2.calc_ivs_gen3()
                formatter = ShowdownFormatter(poke2)
                format = formatter.format()
                self.assertEqual(format, 'Blissey \nLevel: 95 \nEVs: 64 Atk / 56 SpA / 108 SpD / 28 Spe / 252 HP \nSassy Nature \nIVs: 10 Atk / 13 Def / 18 SpA / 25 SpD / 16 Spe / 28 HP \n')



if __name__ == "__main__":
        unittest.main()