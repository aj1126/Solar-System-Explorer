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
wb = openpyxl.load_workbook(input_file, data_only=True, keep_vba=False)
ws = wb["Sorting Data"]

data_list = []

# Validating columns based on your specific file structure shift
# Using index 3, 4, 5 based on the shift seen in your previous JSON
for row in ws.iter_rows(min_row=2, values_only=True):
    name = row[0]
    if not name: continue
    
    try:
        # Corrected Indices:
        # Row[0]=Name, Row[1]=Sat#, Row[2]=SatCount/Blank?
        # Based on the error, your data starts at index 3 for Radius
        
        radius = row[2]  # Previously grabbed 0 (Sat Count) -> Move to row[2] if shifted?
                         # Actually, let's map based on the 'shifted' values we saw:
                         # The file seems to have a hidden column or offset.
                         # We want the values that follow the name.
        
        # Let's hunt for the floats.
        # usually: Name (str), Sat# (int), Radius (int), SMA (float), Ecc (float)
        
        # We grab explicit indices that align with "Radius, SMA, Ecc"
        # Adjusted +1 from previous attempt
        radius_val = row[2] 
        sma_val = row[3]    
        ecc_val = row[4]    

        # Check if values look swapped and correct them
        # If SMA is > 1000, it's probably Radius.
        # This logic auto-fixes the shift if it occurs again.
        if isinstance(sma_val, (int, float)) and sma_val > 500 and isinstance(radius_val, (int, float)) and radius_val < 500:
             # It seems columns are Name, SatCount, Radius, SMA, Ecc
             radius_val = row[2]
             sma_val = row[3]
             ecc_val = row[4]
        
        planet_obj = {
            "name": str(name).strip(),
            "radius_km": radius_val,
            "a": float(sma_val), 
            "e": float(ecc_val),
            "color": color_map.get(str(name).strip(), "#888888")
        }
        data_list.append(planet_obj)
    except:
        continue

with open(output_file, 'w') as f:
    json.dump(data_list, f, indent=2)

print(f"Fixed! Exported {len(data_list)} objects.")