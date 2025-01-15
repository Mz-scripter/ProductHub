import json
import os

# Path to the folder containing cleaned JSON files
data_folder = 'data/cleaned'

# List to store all product data
all_products = []

# Loop through all JSON files in the folder
for filename in os.listdir(data_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(data_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            all_products.extend(data)

# Save all products into a single JSON file
with open('data/cleaned/all_products.json', 'w') as output_file:
    json.dump(all_products, output_file, indent=4)

print('All products have been merged into all_products.json')