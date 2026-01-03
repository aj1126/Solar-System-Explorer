import openpyxl
import json

input_file = 'Solar System Explorer v1.4.xlsm'
output_file = 'solar_system_data.json'

# Standard coloring map
color_map = {
    "Mercury": "#A9A9A9", "Venus": "#FFC966", "Earth": "#4DA6FF", "Mars": "#FF9933",
    "Jupiter": "#FF9966", "Saturn": "#FFD966", "Uranus": "#66CCCC", "Neptune": "#3366FF",
    "Pluto": "#9966CC", "Ceres": "#9966CC", "Eris": "#9966CC", "Vesta": "#CCCC99"
}

print(f"Loading {input_file}...")
# Use data_only=True so we get the calculated numbers, not formulas
wb = openpyxl.load_workbook(input_file, data_only=True, keep_vba=False)
ws = wb["Sorting Data"]

data_list = []

# Iterate starting from row 2 to skip headers
for row in ws.iter_rows(min_row=2, values_only=True):
    # Based on the Screenshot analysis:
    # row[0] = Symbol (Col A)
    # row[1] = Name (Col B)
    # row[2] = Sat # (Col C)
    # row[3] = Radius (Col D)
    # row[4] = SMA (Col E)
    # row[5] = Eccentricity (Col F)
    
    # We grab the Name from index 1
    name_val = row[1]
    
    if not name_val: 
        continue
    
    try:
        radius_val = row[3]  # Column D
        sma_val = row[4]     # Column E
        ecc_val = row[5]     # Column F
        
        # Ensure we have valid numbers
        if isinstance(sma_val, (int, float)) and isinstance(ecc_val, (int, float)):
            planet_obj = {
                "name": str(name_val).strip(),
                "radius_km": radius_val,
                "a": float(sma_val), 
                "e": float(ecc_val),
                "color": color_map.get(str(name_val).strip(), "#888888")
            }
            data_list.append(planet_obj)
    except IndexError:
        # End of valid data
        continue
    except Exception as e:
        print(f"Skipping row {name_val}: {e}")
        continue

with open(output_file, 'w') as f:
    json.dump(data_list, f, indent=2)

print(f"Fixed! Exported {len(data_list)} objects correctly.")