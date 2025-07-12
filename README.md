# geopy-distance-calculator
A simple Python tool to calculate geodesic distances from coordinates in Excel using geopy.

# 🗺️ Geopy Distance Calculator

This Python script calculates the **geodesic distance** (in kilometers) between a fixed reference point and geographic coordinates stored in an Excel file. It's built using the `pandas` and `geopy` libraries and is useful for geospatial analysis, mapping, or OSINT workflows.

---

📌 Features

- 📄 Reads Excel files with `latitude` and `longitude` columns
- 📍 Uses a customizable fixed reference point (Kyiv by default)
- 📏 Calculates distance for each row using `geopy`
- 📤 Saves results with a new `distance_km` column in a new Excel file
- 🛠️ User specifies both input and output file paths at runtime

---

⚙️ Requirements

Install dependencies using pip:

```bash
pip install pandas geopy
````

---

📥 Input Format

The input Excel file should contain at least the following two columns:

| latitude | longitude |
| -------- | --------- |
| 50.4501  | 30.5234   |
| 47.8517  | 35.1171   |

Other columns are allowed, but `latitude` and `longitude` are required and must be non-empty.

---

▶️ How to Use

Run the script from your terminal or command prompt:

```bash
python distance_calculator.py
```

You will be prompted to:

1. **Enter the path to the input Excel file**
2. **Enter the desired output Excel file path**

Example input:

```
Enter path to input Excel file: /Users/yourname/Documents/input.xlsx
Enter path for output Excel file: /Users/yourname/Documents/output_with_distances.xlsx
```

After processing, the output Excel file will contain a new column:

| latitude | longitude | ... | distance\_km |
| -------- | --------- | --- | ------------ |
| 50.4501  | 30.5234   | ... | 0.28         |
| 47.8517  | 35.1171   | ... | 446.55       |

---

🧭 Reference Point

To change the reference point (e.g., to Berlin), modify this line in `distance_calculator.py`:

```python
REFERENCE_COORDS = (52.5200, 13.4050)  # Berlin
```

---

📁 Output

* A new Excel file with the same data plus a `distance_km` column.
* The file is saved to the path you specify during runtime.

---

## 📄 License

This project is licensed under the MIT License.
