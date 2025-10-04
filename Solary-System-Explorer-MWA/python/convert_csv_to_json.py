import csv
import json

def convert_csv_to_json(csv_filepath, json_filepath):
    """
    Reads a CSV file and converts it to a JSON array,
    casting data types according to the celestial body schema.
    """
    json_array = []

    # Open the CSV file for reading
    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        # Use DictReader to read rows as dictionaries
        csv_reader = csv.DictReader(csv_file)

        # Process each row in the CSV
        for row in csv_reader:
            # Create a correctly typed dictionary for each planet
            planet_object = {
                "name": row["name"],
                "satellites": int(row["satellites"]), # Cast to integer
                "radius_km": float(row["radius_km"]), # Cast to float/number
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

    # Open the JSON file for writing
    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        # Dump the array into the JSON file with nice formatting
        json.dump(json_array, json_file, indent=4)

    print(f"Successfully converted {csv_filepath} to {json_filepath}!")

# --- Run the conversion ---
# Make sure 'planets.csv' is in the same directory as this script.
# The output will be 'planets.json'.
# Old line at the bottom of the script
# convert_csv_to_json('planets.csv', 'planets.json')
# New line using a relative path
convert_csv_to_json('../csv_folder/planets.csv', 'planets.json')