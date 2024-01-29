input_file_path = "ClassNames.txt"
output_file_path = "types.xml"

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    output_file.write('<types>\n')

    for line in input_file:
        line = line.strip()

        if line.startswith("##"):
            # Skip lines starting with ##
            continue

        if line.startswith("crsk"):
            lifetime = 86400
        else:
            lifetime = 1800

        output_file.write(f'  <type name="{line}">\n')
        output_file.write(f'    <nominal>0</nominal>\n')
        output_file.write(f'    <lifetime>{lifetime}</lifetime>\n')
        output_file.write(f'    <restock>0</restock>\n')
        output_file.write(f'    <min>0</min>\n')
        output_file.write(f'    <flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0" />\n')
        output_file.write(f'  </type>\n')

    output_file.write('</types>\n')

print(f'XML file generated at {output_file_path}')
