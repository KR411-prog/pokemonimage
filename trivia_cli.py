import json
import requests
import argparse
import urllib.request
from PIL import Image

data = {}
j=0

for i in range(1,20):
    url_pokemon = "https://pokeapi.co/api/v2/pokemon/"+str(i)
    response = requests.get(url=url_pokemon)
    content = response.json()
    data[content["name"]] = content["sprites"]["front_default"]

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
args = parser.parse_args()
print(f"Hello {args.name}")

try:
    png_name = args.name+".png"
    print(data[args.name])
    urllib.request.urlretrieve(data[args.name],png_name)
    img = Image.open(png_name)
    img.show()
except(Exception):
    print("Error happened")
