# Python Script to Extract Classnames from config.cpp

# Input and output file paths
input_file_path = "config.cpp"
output_file_path = "ClassNames.txt"

# Read the content of the input file
with open(input_file_path, "r") as file:
    content = file.read()

# Find the start index of "class CfgVehicles"
start_index = content.find("class CfgVehicles")

# Set the end index to the end of the file
end_index = len(content)

# Extract the content between "class CfgVehicles" and the closing bracket
cfg_vehicles_content = content[start_index:end_index]

# Find all occurrences of "class" within "class CfgVehicles"
class_occurrences = [occurrence.strip() for occurrence in cfg_vehicles_content.split("class ")[1:]]

# Extract the class names without ';' or ':'
class_names = []
for occurrence in class_occurrences:
    class_name = occurrence.split()[0].rstrip(';').rstrip(':')
    class_names.append(class_name)

# Write the extracted classnames to the output file
with open(output_file_path, "w") as file:
    file.write("\n".join(class_names))

print(f"Classnames extracted and saved to {output_file_path}")
