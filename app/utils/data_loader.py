import json

def load_products():
    with open('app/data/all_products.json', 'r', encoding='utf-8') as file:
        return json.load(file)

products_data = load_products()