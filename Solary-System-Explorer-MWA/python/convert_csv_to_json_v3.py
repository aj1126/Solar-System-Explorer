import csv
import json
from pathlib import Path
import re # Import the regular expression module

def clean_and_extract_number(text):
    """
    Removes commas and extracts the first number (integer or float) from a string.
    Returns '0' if no number is found.
    """
    if not isinstance(text, str):
        return '0'
    
    # First, remove any commas to handle thousands separators (e.g., "1,234")
    text_no_commas = text.replace(',', '')
    
    # Find the first sequence of characters that looks like a number
    # This pattern handles optional negative signs, integers, and decimals
    match = re.search(r'(-?\d+\.?\d*)', text_no_commas)
    
    if match:
        return match.group(0)
    else:
        return '0' # Return a default value if no number is found

def convert_csv_to_json(csv_filepath, json_filepath):
    """
    Reads a CSV, ignoring the first column, cleans numeric data, and converts it to a JSON array.
    """
    json_array = []
    with open(csv_filepath, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)[1:]

        for row in csv_reader:
            data_values = row[1:]
            planet_data = dict(zip(header, data_values))

            # Clean the string data before converting to a number
            planet_object = {
                "name": planet_data["name"],
                "satellites": int(clean_and_extract_number(planet_data["satellites"])),
                "radius_km": float(clean_and_extract_number(planet_data["radius_km"])),
                "semi_major_axis_au": float(clean_and_extract_number(planet_data["semi_major_axis_au"])),
                "eccentricity": float(clean_and_extract_number(planet_data["eccentricity"])),
                "inclination_deg": float(clean_and_extract_number(planet_data["inclination_deg"])),
                "argument_of_periapsis_deg": float(clean_and_extract_number(planet_data["argument_of_periapsis_deg"])),
                "longitude_of_ascending_node_deg": float(clean_and_extract_number(planet_data["longitude_of_ascending_node_deg"])),
                "mean_anomaly_deg": float(clean_and_extract_number(planet_data["mean_anomaly_deg"])),
                "density_g_cm3": float(clean_and_extract_number(planet_data["density_g_cm3"])),
                "type": planet_data["type"]
            }
            json_array.append(planet_object)
    
    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        json.dump(json_array, json_file, indent=4)

    print(f"Successfully converted and cleaned {csv_filepath} to {json_filepath}!")

# --- Define paths and run the conversion ---
SCRIPT_DIR = Path(__file__).parent
PARENT_DIR = SCRIPT_DIR.parent
CSV_FOLDER = PARENT_DIR / "csv_folder"
JSON_OUTPUT_FOLDER = PARENT_DIR



csv_file_path = CSV_FOLDER / "SolarSystem-extracted.csv"
json_file_path = JSON_OUTPUT_FOLDER / "SolarSystem-extracted.json"

convert_csv_to_json(csv_file_path, json_file_path)