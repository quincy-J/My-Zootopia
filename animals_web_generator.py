import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

animals = load_data("animals_data.json")

for animal in animals:
    if "name" in animal:
        print(f"Name: {animal['name']}")
    if "diet" in animal:
        print(f"Diet: {animal['diet']}")
    if "locations" in animal and len(animal["locations"]) > 0:
        print(f"Location: {animal['locations'][0]}")
    if "type" in animal:
        print(f"Type: {animal['type']}")

    print()