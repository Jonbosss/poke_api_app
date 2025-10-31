import requests
from PIL import Image
from io import BytesIO

base_url = "https://pokeapi.co/api/v2/"
image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/136.png"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


# def display_pokemon_image(id):
image_response = requests.get(image_url)

# if response.status_code == 200:
#     pokemon_data = response.json()
#     return pokemon_data
# else:
#     print(f"Failed to retrieve data {response.status_code}")
#
#
pokemon_name = "flareon"
pokemon_info = get_pokemon_info(pokemon_name)
img = Image.open(BytesIO(image_response.content))

# f"{pokemon_info["sprites"]["front_default"]}"
# pokemon_image = get_pokemon_image("id")

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"# {pokemon_info["id"]}")
    if (len(pokemon_info["types"])) > 1:
        print(
            f"Types: {pokemon_info["types"][0]["type"]["name"].capitalize()}" f" and {pokemon_info["types"][1]["type"]["name"].capitalize()}")
    else:
        print(
            f"Type: {pokemon_info["types"][0]["type"]["name"].capitalize()}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
    img.show(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/136.png")
