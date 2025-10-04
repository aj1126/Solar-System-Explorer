import csv
import json
from pathlib import Path


## How It Works
# Use csv.reader: Instead of DictReader, we use csv.reader, which treats each row as a simple list.
# Process Header: header = next(csv_reader)[1:] reads the first row (the header) and immediately slices it to discard the first column's name.
# Process Data Rows: For every subsequent row, data_values = row[1:] does the same thing, creating a new list that contains all values except the first one.
# Create Dictionary: dict(zip(header, data_values)) cleverly combines the corrected header with the corrected data row to create a dictionary, just like DictReader did before.
# Type Casting: The rest of the script then proceeds as normal, using the keys from that dictionary to create the final JSON object with the correct data types.

def convert_csv_to_json(csv_filepath, json_filepath):
    """
    Reads a CSV, ignoring the first column, and converts it to a JSON array,
    casting data types according to the celestial body schema.
    """
    json_array = []
    with open(csv_filepath, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Read the header row, but skip the first column's name
        header = next(csv_reader)[1:]

        # Process each data row in the CSV
        for row in csv_reader:
            # Skip the first column's data by slicing the list from the second item onwards
            data_values = row[1:]
            
            # Create a dictionary by zipping the header with the corresponding data values
            planet_data = dict(zip(header, data_values))

            # Create the final, correctly typed object
            # This ensures if the column order changes, it still works correctly
            planet_object = {
                "name": planet_data["name"],
                "satellites": int(planet_data["satellites"]),
                "radius_km": float(planet_data["radius_km"]),
                "semi_major_axis_au": float(planet_data["semi_major_axis_au"]),
                "eccentricity": float(planet_data["eccentricity"]),
                "inclination_deg": float(planet_data["inclination_deg"]),
                "argument_of_periapsis_deg": float(planet_data["argument_of_periapsis_deg"]),
                "longitude_of_ascending_node_deg": float(planet_data["longitude_of_ascending_node_deg"]),
                "mean_anomaly_deg": float(planet_data["mean_anomaly_deg"]),
                "density_g_cm3": float(planet_data["density_g_cm3"]),
                "type": planet_data["type"]
            }
            json_array.append(planet_object)
    
    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        json.dump(json_array, json_file, indent=4)

    print(f"Successfully converted {csv_filepath} to {json_filepath}, ignoring the first column!")

# --- Define paths relative to THIS script's location ---
SCRIPT_DIR = Path(__file__).parent
PARENT_DIR = SCRIPT_DIR.parent
CSV_FOLDER = PARENT_DIR / "csv_folder"
JSON_OUTPUT_FOLDER = PARENT_DIR

# --- Construct the full paths ---
csv_file_path = CSV_FOLDER / "SolarSystem-extracted.csv"
json_file_path = JSON_OUTPUT_FOLDER / "SolarSystem-extracted.json"

# --- Run the conversion ---
convert_csv_to_json(csv_file_path, json_file_path)