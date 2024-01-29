import json

input_file_path = "Vehicles.json"
output_file_path = "cfgSpawnableTypes.xml"

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    output_file.write('<types>\n')

    data = json.load(input_file)
    for vehicle_data in data:
        vehicle_name = vehicle_data["VehicleName"]
        output_file.write(f'  <type name="{vehicle_name}">\n')

        for part in vehicle_data["VehicleParts"]:
            output_file.write(f'    <attachments chance="1.00">\n')
            output_file.write(f'      <item name="{part}" chance="1" />\n')
            output_file.write(f'    </attachments>\n')

        output_file.write(f'  </type>\n')

    output_file.write('</types>\n')

print(f'XML file generated at {output_file_path}')
