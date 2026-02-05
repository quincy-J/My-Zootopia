import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

animals = load_data("animals_data.json")

output = ""

for animal in animals:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    type_ = animal.get("characteristics", {}).get("type")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None

    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{name}</div>\n'
    output += '<p class="card__text">'

    if diet:
        output += f'<strong>Diet:</strong> {diet}<br/>\n'
    if location:
        output += f'<strong>Location:</strong> {location}<br/>\n'
    if type_:
        output += f'<strong>Type:</strong> {type_}<br/>\n'

    output += '</p></li>\n'

with open("animals_template.html", "r") as file:
    template = file.read()

html_output = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(html_output)

print("animals.html wurde aktualisiert.")