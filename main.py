import math
from collections import OrderedDict
from pprint import pprint

import pandas as pd
import numpy as np

from pokemon import Pokemon

dictionary = {}
pokemon_distances = {}


def create_pokemon(row):
    pkmn = Pokemon(row[0], row[1].lower(), row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
    return pkmn


def process_pokemon(filename):
    file = pd.read_csv(filename, sep=",")

    zipp = zip(file['# Dex'], file[' Pokemon (name)'], file[' complexity'], file[' realism'],
               file[' artificiality'], file[' fantasy'], file[' humanoid'], file[' cuteness'],
               file[' coolness'], file[' beauty'], file[' popularity'])

    all_pokemon = [create_pokemon(row) for row in zipp]

    for pokemon in all_pokemon:
        if pokemon.is_valid():
            if pokemon.name in dictionary:
                dictionary[pokemon.name]["num_of"] += 1
                dictionary[pokemon.name]["complexity"] += pokemon.complexity
                dictionary[pokemon.name]["realism"] += pokemon.realism
                dictionary[pokemon.name]["artificiality"] += pokemon.artificiality
                dictionary[pokemon.name]["fantasy"] += pokemon.fantasy
                dictionary[pokemon.name]["humanoid"] += pokemon.humanoid
                dictionary[pokemon.name]["cuteness"] += pokemon.cuteness
                dictionary[pokemon.name]["coolness"] += pokemon.coolness
                dictionary[pokemon.name]["beauty"] += pokemon.beauty
                dictionary[pokemon.name]["popularity"] += pokemon.popularity
            else:
                dictionary[pokemon.name] = ({
                    "num_of": 1,
                    "complexity": pokemon.complexity,
                    "realism": pokemon.realism,
                    "artificiality": pokemon.artificiality,
                    "fantasy": pokemon.fantasy,
                    "humanoid": pokemon.humanoid,
                    "cuteness": pokemon.cuteness,
                    "coolness": pokemon.coolness,
                    "beauty": pokemon.beauty,
                    "popularity": pokemon.popularity,
                })

    for pokemon in dictionary:
        num_of = dictionary[pokemon]["num_of"]
        dictionary[pokemon]["complexity"] /= num_of
        dictionary[pokemon]["realism"] /= num_of
        dictionary[pokemon]["artificiality"] /= num_of
        dictionary[pokemon]["fantasy"] /= num_of
        dictionary[pokemon]["humanoid"] /= num_of
        dictionary[pokemon]["cuteness"] /= num_of
        dictionary[pokemon]["coolness"] /= num_of
        dictionary[pokemon]["beauty"] /= num_of
        dictionary[pokemon]["popularity"] /= num_of


# print(dictionary["wellspring mask ogerpon"])

# euclidean distance for now
def calc_distances(user_input: []):
    for pokemon in dictionary:
        distance = 0
        distance += abs(dictionary[pokemon]["complexity"] - user_input[0]) ** 2
        distance += abs(dictionary[pokemon]["realism"] - user_input[1]) ** 2
        distance += abs(dictionary[pokemon]["artificiality"] - user_input[2]) ** 2
        distance += abs(dictionary[pokemon]["fantasy"] - user_input[3]) ** 2
        distance += abs(dictionary[pokemon]["humanoid"] - user_input[4]) ** 2
        distance += abs(dictionary[pokemon]["cuteness"] - user_input[5]) ** 2
        distance += abs(dictionary[pokemon]["coolness"] - user_input[6]) ** 2
        distance += abs(dictionary[pokemon]["beauty"] - user_input[7]) ** 2
        distance += abs(dictionary[pokemon]["popularity"] - user_input[8]) ** 2
        distance = math.sqrt(distance)
        pokemon_distances[pokemon] = distance


def sort_1d_dictionary_output_keys(dictionary: {object: float}) -> [object]:
    """
    Used to sort a 1D dictionary by the value of its elements in descending order
    :param dictionary: dictionary in format {key, value}
    :return: List of the keys in descending order
    """
    dict_list = [(k, v) for k, v in dictionary.items()]
    sorted_list = sorted(dict_list, key=lambda x: x[1], reverse=True)[slice(10)]
    keys = [x[0] for x in sorted_list]  # Extract document IDs
    return keys


def main():

    process_pokemon("data/all-ratings.csv")
    print("Hello there! Welcome to the world of POKEMON! My name is OAK! People call me the POKEMON PROF! \n"
          "This world is inhabited by creatures called POKEMON! For some people, POKEMON are pets. \n"
          "Others use them for fights. Myself...I study POKEMON as a profession. \n"
          "Today, we are going to decide the ideal partner POKEMON for you!\n\n"
          "Please answer the following on a scale of 1-5")

    complexity = float(input("How COMPLEX do you want it to be? "))
    realism = float(input("How REALISTIC do you want it to be? "))
    artificiality = float(input("How ARTIFICIAL do you want it to be? "))
    fantasy = float(input("How FANTASTICAL do you want it to be? "))
    humanoid = float(input("How HUMANOID do you want it to be? "))
    cuteness = float(input("How CUTE do you want it to be? "))
    coolness = float(input("How COOL do you want it to be? "))
    beauty = float(input("How BEAUTIFUL do you want it to be? "))
    popularity = float(input("How POPULAR do you want it to be? "))


    calc_distances([complexity, realism, artificiality, fantasy, humanoid, cuteness, coolness, beauty, popularity])

    sorted_dict = sorted(pokemon_distances.items(), key=lambda x:x[1], reverse=False)[slice(5)]

    print(f"\nOKAY! the top 5 most suitable POKEMON for you are:")

    for i in range(5):
        print(f"{i+1}: {sorted_dict[i][0].upper()}")
