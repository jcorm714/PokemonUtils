from Pokemon import Pokemon
from Nature import Nature
from Showdown_Formatter import Showdown_Formatter


def main():
        poke = Pokemon()
        poke.name = "Flaaffy"
        poke.nature = Nature.TIMID
        poke.level = 45
        poke.set_base_stats(atk=55,def_=55, spa=80, spd=60,spe=45,hp=70)
        poke.set_evs(atk=48,def_=36,spa=172,spd=80,spe=76, hp=96)
        poke.set_stat_totals(atk=63,def_=67,spa=108,spd=79,spe=70,hp=140)
        poke.calc_ivs_gen3()
        formatter = Showdown_Formatter(poke)
        print(formatter.format())

if __name__ == "__main__":
        main()