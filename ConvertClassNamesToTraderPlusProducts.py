input_file_path = "YourClassNamesList.txt" # Ändere dies nach Bedarf
output_file_path = "TraderPlusPriceConfig.json" # Ändere dies nach Bedarf

formatted_entries = []
categories = []

with open(input_file_path, 'r') as input_file:
    lines = input_file.read().splitlines()

for line in lines:
    # Ignoriere leere Zeilen
    if not line.strip():
        continue

    # Überprüfe, ob die Zeile mit "##" oder "//" beginnt, und behandle sie als Kategorie
    if line.startswith("##") or line.startswith("//"):
        category_name = line.lstrip("#/").strip()
        categories.append({
            "CategoryName": category_name,
            "Products": []
        })
        continue

    # Füge das Produkt zur formatierten Liste der aktuellen Kategorie hinzu
    formatted_entry = f'{line},1,-1,1,150,5'
    if categories:
        categories[-1]["Products"].append(formatted_entry)

# Schreibe die formatierten Einträge in die Ausgabedatei im JSON-Format
with open(output_file_path, 'w') as output_file:
    output_file.write("[\n")
    for i, category in enumerate(categories):
        output_file.write('  {\n')
        output_file.write(f'    "CategoryName": "{category["CategoryName"]}",\n')
        output_file.write('    "Products": [\n')
        output_file.write(',\n'.join([f'      "{product}"' for product in category["Products"]]))
        output_file.write('\n    ]\n  }')
        if i < len(categories) - 1:
            output_file.write(',')
        output_file.write('\n')
    output_file.write("]\n")

print(f'Finished! Outputfile: "{output_file_path}".')
