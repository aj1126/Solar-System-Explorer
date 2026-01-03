import openpyxl
import json
import os

input_file = 'Solar System Explorer v1.4.xlsm'
output_file = 'solar_system_data.json'

# Standard coloring map
color_map = {
    "Mercury": "#A9A9A9", "Venus": "#FFC966", "Earth": "#4DA6FF", "Mars": "#FF9933",
    "Jupiter": "#FF9966", "Saturn": "#FFD966", "Uranus": "#66CCCC", "Neptune": "#3366FF",
    "Pluto": "#9966CC", "Ceres": "#9966CC", "Eris": "#9966CC", "Vesta": "#CCCC99"
}

print(f"Loading {input_file}...")

if not os.path.exists(input_file):
    print("ERROR: Excel file not found in this folder!")
else:
    # Use data_only=True to get values, not formulas
    wb = openpyxl.load_workbook(input_file, data_only=True, keep_vba=False)
    ws = wb["Sorting Data"]

    data_list = []

    # Iterate starting from row 2 to skip headers
    for row in ws.iter_rows(min_row=2, values_only=True):
        # CORRECT MAPPING BASED ON YOUR SCREENSHOTS:
        # Col A [0]: Symbol
        # Col B [1]: Name
        # Col C [2]: Satellites
        # Col D [3]: Radius (km)
        # Col E [4]: SMA (AU)
        # Col F [5]: Eccentricity
        
        name_val = row[1]
        
        if not name_val: 
            continue
        
        try:
            radius_val = row[3]  # Column D
            sma_val = row[4]     # Column E
            ecc_val = row[5]     # Column F
            
            # Data Cleaning: Ensure we have floats
            if isinstance(sma_val, (int, float)) and isinstance(ecc_val, (int, float)):
                planet_obj = {
                    "name": str(name_val).strip(),
                    "radius_km": radius_val,
                    "a": float(sma_val), 
                    "e": float(ecc_val),
                    "color": color_map.get(str(name_val).strip(), "#888888")
                }
                data_list.append(planet_obj)
                
                # DEBUG PRINT: Verify Mercury is correct
                if "Mercury" in str(name_val):
                    print(f"DEBUG CHECK: Mercury SMA is {sma_val} (Should be ~0.387)")
                    print(f"DEBUG CHECK: Mercury Radius is {radius_val} (Should be ~2440)")

        except Exception as e:
            continue

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data_list, f, indent=2)

    print(f"SUCCESS! Exported {len(data_list)} objects to {output_file}")