import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "flareon"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
    if (len(pokemon_info["types"])) > 1:
        print(
        f"Types: {pokemon_info["types"][0]["type"]["name"].capitalize()}" f" and {pokemon_info["types"][1]["type"]["name"].capitalize()}")
    else:
        print(
        f"Type: {pokemon_info["types"][0]["type"]["name"].capitalize()}")
