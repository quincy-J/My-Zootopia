import json


def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


def serialize_animal(animal):
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    type_ = animal.get("characteristics", {}).get("type")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None

    html = '<li class="cards__item">\n'
    html += f'<div class="card__title">{name}</div>\n'
    html += '<p class="card__text">'

    if diet:
        html += f'<strong>Diet:</strong> {diet}<br/>\n'
    if location:
        html += f'<strong>Location:</strong> {location}<br/>\n'
    if type_:
        html += f'<strong>Type:</strong> {type_}<br/>\n'

    html += '</p></li>\n'
    return html


def build_html_page(data, template_path, output_path):
    items_html = ""

    for animal in data:
        items_html += serialize_animal(animal)

    with open(template_path, "r") as file:
        template = file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", items_html)

    with open(output_path, "w") as file:
        file.write(final_html)


def main():
    animals = load_data("animals_data.json")
    build_html_page(
        data=animals,
        template_path="animals_template.html",
        output_path="animals.html"
    )
    print("animals.html wurde aktualisiert.")


if __name__ == "__main__":
    main()