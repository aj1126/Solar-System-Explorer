###### [AI Generated | Gemni 3 Pro]  

<!-- Here is a clean, step-by-step `README.md` file designed for your fork. It separates the "Just let me view it" users from the "I want to edit the data" users, which minimizes trouble for the average person.

You can create a file named `README.md` in your folder and paste this content directly into it.
 -->
---

# Solar System Explorer (Web Port)

An interactive D3.js visualization of the Solar System, ported from the [original Excel-based project](https://www.google.com/search?q=https://github.com/amorphose/Solar-System-Explorer). This version runs in a web browser, allowing for smoother performance, zooming, and cross-platform compatibility without needing Excel macros.

## 🚀 Quick Start (Just viewing the map)

If you just want to explore the solar system map, you only need Python installed to run a local web server.

### 1. Prerequisites

* **Python:** Most computers have this installed. You can check by opening your Terminal (or PowerShell on Windows) and typing `python --version`.
* *If not installed:* Download it from [python.org](https://www.python.org/downloads/).



### 2. Run the Viewer

1. Download or Clone this repository to your computer.
2. Open the folder in **File Explorer**.
3. Right-click empty space and select **"Open in Terminal"**.
4. Type the following command and press **Enter**:
```powershell
python -m http.server

```


*(If that doesn't work, try `py -m http.server`)*
5. Open your web browser and go to:
**[http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)**
6. **Done!** You can now scroll to zoom and drag to pan around the solar system.
* *To stop the server:* Go back to the terminal and press `Ctrl + C`.



---

## 🛠️ Developer Guide (Updating the Data)

If you want to modify the source Excel file (`Solar System Explorer v1.4.xlsm`) and update the web visualization, follow these steps.

### 1. Setup Your Environment (One-time setup)

You need to install the `openpyxl` library to read the Excel file.

1. Open your Terminal in the project folder.
2. Create a virtual environment (keeps your system clean):
```powershell
python -m venv venv

```


3. Activate the environment:
```powershell
.\venv\Scripts\activate

```


*(You will see `(venv)` appear at the start of your command line)*
4. Install the required library:
```powershell
pip install openpyxl

```



### 2. Exporting New Data

Whenever you change the Excel file, run the conversion script to generate a new JSON file for the website:

1. Make sure your virtual environment is active (`(venv)` is visible).
2. Run the fix script:
```powershell
python export_fix.py

```


3. This updates `solar_system_data.json`.
4. Refresh your browser (`Ctrl + F5`) to see the changes.

---

## 📂 Project Structure

* `index.html` - The main entry point for the visualization.
* `solar_system_data.json` - The database of planets and orbits (generated from Excel).
* `export_fix.py` - Python script to convert Excel data to JSON.
* `Solar System Explorer v1.4.xlsm` - The original source data (Excel).

## 📜 Credits

* **Original Excel Project:** S. Bianchini (amorphose)
* **Font:** Robert Winslow (Astromoony)
* **Data Sources:** NASA JPL Small-Body Database, Mike Brown’s Dwarf Planet List.
* **Web Port:** A. Jukes III ([aj1126](https://github.com/aj1126))