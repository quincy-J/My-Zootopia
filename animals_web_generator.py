import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

# 1. JSON laden
animals = load_data("animals_data.json")

# 2. HTML-String erzeugen
output = ""

for animal in animals:
    name = animal.get("name")
    diet = animal.get("diet")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None
    type_ = animal.get("type")

    output += '<li class="cards__item">\n'

    if name:
        output += f"Name: {name}<br/>\n"
    if diet:
        output += f"Diet: {diet}<br/>\n"
    if location:
        output += f"Location: {location}<br/>\n"
    if type_:
        output += f"Type: {type_}<br/>\n"

    output += '</li>\n\n'

# 3. Template laden
with open("animals_template.html", "r") as file:
    template = file.read()

# 4. Platzhalter ersetzen
html_output = template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. Neue Datei schreiben
with open("animals.html", "w") as file:
    file.write(html_output)

print("animals.html wurde aktualisiert.")