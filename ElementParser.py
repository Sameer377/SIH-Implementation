import xml.etree.ElementTree as ET
import json

# Define the path to your dumped XML file
xml_file_path = 'Ui.xml'
json_output_path = 'ui_signature.json'

# Load and parse the XML file
try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
except FileNotFoundError:
    print(f"Error: The file {xml_file_path} was not found.")
    exit(1)
except ET.ParseError:
    print(f"Error: The file {xml_file_path} could not be parsed.")
    exit(1)

# Initialize a dictionary to hold the UI signature
ui_signature = {
    "bottom_navigation": {},
    "feed": []
}

# Iterate through nodes and extract necessary data
for node in root.iter('node'):
    resource_id = node.get('resource-id')
    bounds = node.get('bounds')
    class_name = node.get('class')
    text = node.get('text')

    # Check for bottom navigation items (you may need to adjust this condition)
    if resource_id and 'nav_' in resource_id:
        ui_signature['bottom_navigation'][resource_id] = {
            "resource_id": resource_id,
            "bounds": bounds
        }
    # Assuming feed posts are represented by ImageView or other classes
    elif class_name == 'android.widget.ImageView' or class_name == 'android.widget.FrameLayout':
        ui_signature['feed'].append({
            "resource_id": resource_id,
            "bounds": bounds,
            "text": text  # Include text if needed
        })

# Save the UI signature to a JSON file
with open(json_output_path, 'w') as json_file:
    json.dump(ui_signature, json_file, indent=4)

print(f"UI signature extracted and saved to {json_output_path}.")
