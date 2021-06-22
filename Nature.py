"""This file holds information pertaining to natures. It also has the functionality to return
the positive and negative modifiers to a pokemon's stats"""

from enum import Enum
import typing

from Pokemon import Stats


class Nature(Enum):
        """An Enum representing the list of pokemon antures"""
        HARDY = "Hardy"
        LONELY = "Lonely"
        BRAVE = "Brave"
        ADAMANT = "Adamant"
        NAUGHTY = "Naughty"
        BOLD = "Bold"
        DOCILE = "Docile"
        RELAXED = "Relaxed"
        IMPISH = "Impish"
        LAX = "Lax"
        TIMID = "Timid"
        HASTY = "Hasty"
        SERIOUS = "Serious"
        JOLLY = "Jolly"
        NAIVE = "Naive"
        MODEST = "Modest"
        MILD = "Mild"
        QUIET = "Quiet"
        BASHFUL = "Bashful"
        RASH = "Rash"
        CALM = "Calm"
        GENTLE = "Gentle"
        SASSY = "Sassy"
        CAREFUL = "Careful"
        QUIRKY = "Quirky"

NatureModifiers = dict[str]

def get_affected_stats(nature: Nature) -> NatureModifiers:
        """Returns the positive and negative stat affected by a nature
        Parameters
        ----------
        nature: Nature
                An enumeration of the pokemon natures
        returns
                dictionary called modifiers with positive and negative stat modifed
                if the nature is neutral the dictionary will be empty
                keys:
                        POS
                        NEG"""
        modifiers = {"POS": "", "NEG": ""}
        if nature == Nature.LONELY:
                modifiers["POS"] = Stats.ATTACK
                modifiers["NEG"] = Stats.DEFENSE
        elif nature == Nature.BRAVE:
                modifiers["POS"] = Stats.ATTACK
                modifiers["NEG"] = Stats.SPEED
        elif nature == Nature.ADAMANT:
                modifiers["POS"] = Stats.ATTACK
                modifiers["NEG"] = Stats.SP_ATTACK
        elif nature == Nature.NAUGHTY:
                modifiers["POS"] = Stats.ATTACK
                modifiers["NEG"] = Stats.DEFENSE
        elif nature == Nature.BOLD:
                modifiers["POS"] = Stats.DEFENSE
                modifiers["NEG"] = Stats.ATTACK
        elif nature == Nature.RELAXED:
                modifiers["POS"] = Stats.DEFENSE
                modifiers["NEG"] = Stats.SPEED
        elif nature == Nature.IMPISH:
                modifiers["POS"] = Stats.DEFENSE
                modifiers["NEG"] = Stats.SP_ATTACK
        elif nature == Nature.LAX:
                modifiers["POS"] = Stats.DEFENSE
                modifiers["NEG"] = Stats.SP_DEFENSE
        elif nature == Nature.TIMID:
                modifiers["POS"] = Stats.SPEED
                modifiers["NEG"] = Stats.ATTACK
        elif nature == Nature.HASTY:
                modifiers["POS"] = Stats.SPEED
                modifiers["NEG"] = Stats.DEFENSE
        elif nature == Nature.JOLLY:
                modifiers["POS"] = Stats.SPEED
                modifiers["NEG"] = Stats.SP_ATTACK
        elif nature == Nature.NAIVE:
                modifiers["POS"] = Stats.SPEED
                modifiers["NEG"] = Stats.SP_DEFENSE
        elif nature == Nature.MODEST:
                modifiers["POS"] = Stats.SP_ATTACK
                modifiers["NEG"] = Stats.ATTACK
        elif nature == Nature.MILD:
                modifiers["POS"] = Stats.SP_ATTACK
                modifiers["NEG"] = Stats.DEFENSE
        elif nature == Nature.QUIET:
                modifiers["POS"] = Stats.SP_ATTACK
                modifiers["NEG"] = Stats.SPEED
        elif nature == Nature.RASH:
                modifiers["POS"] = Stats.SP_ATTACK
                modifiers["NEG"] = Stats.SP_DEFENSE
        elif nature == Nature.CALM:
                modifiers["POS"] = Stats.SP_DEFENSE
                modifiers["NEG"] = Stats.ATTACK
        elif nature == Nature.GENTLE:
                modifiers["POS"] = Stats.SP_DEFENSE
                modifiers["NEG"] = Stats.DEFENSE
        elif nature == Nature.SASSY:
                modifiers["POS"] = Stats.SP_DEFENSE
                modifiers["NEG"] = Stats.SPEED
        elif nature == Nature.CAREFUL:
                modifiers["POS"] = Stats.SP_DEFENSE
                modifiers["NEG"] = Stats.SP_ATTACK
        return modifiers



