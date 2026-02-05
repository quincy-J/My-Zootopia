import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

# 1. JSON laden
animals = load_data("animals_data.json")

# 2. String mit allen Tierinfos erzeugen
output = ""

for animal in animals:
    if "name" in animal:
        output += f"Name: {animal['name']}\n"
    if "diet" in animal:
        output += f"Diet: {animal['diet']}\n"
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"Location: {animal['locations'][0]}\n"
    if "type" in animal:
        output += f"Type: {animal['type']}\n"

    output += "\n"

# 3. Template laden
with open("animals_template.html", "r") as file:
    template = file.read()

# 4. Platzhalter ersetzen
html_output = template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. Neue Datei schreiben
with open("animals.html", "w") as file:
    file.write(html_output)

print("animals.html wurde erzeugt.")