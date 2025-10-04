import csv
import json
from pathlib import Path # Import the Path object

def convert_csv_to_json(csv_filepath, json_filepath):
    """
    Reads a CSV file and converts it to a JSON array,
    casting data types according to the celestial body schema.
    """
    json_array = []
    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            planet_object = {
                "name": row["name"],
                "satellites": int(row["satellites"]),
                "radius_km": float(row["radius_km"]),
                "semi_major_axis_au": float(row["semi_major_axis_au"]),
                "eccentricity": float(row["eccentricity"]),
                "inclination_deg": float(row["inclination_deg"]),
                "argument_of_periapsis_deg": float(row["argument_of_periapsis_deg"]),
                "longitude_of_ascending_node_deg": float(row["longitude_of_ascending_node_deg"]),
                "mean_anomaly_deg": float(row["mean_anomaly_deg"]),
                "density_g_cm3": float(row["density_g_cm3"]),
                "type": row["type"]
            }
            json_array.append(planet_object)
    
    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        json.dump(json_array, json_file, indent=4)

    print(f"Successfully converted {csv_filepath} to {json_filepath}!")

# --- Define paths relative to THIS script's location ---
# Path(__file__) is the path to the current script.
# .parent gets the directory the script is in ('python_folder').
# .parent.parent gets the parent of that directory ('parent_folder').
SCRIPT_DIR = Path(__file__).parent
PARENT_DIR = SCRIPT_DIR.parent
CSV_FOLDER = PARENT_DIR / "csv_folder"
JSON_OUTPUT_FOLDER = PARENT_DIR # Let's save the JSON in the parent folder

# --- Construct the full paths ---
csv_file_path = CSV_FOLDER / "planets.csv"
json_file_path = JSON_OUTPUT_FOLDER / "planets.json"

# --- Run the conversion with the new paths ---
convert_csv_to_json(csv_file_path, json_file_path)