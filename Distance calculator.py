import pandas as pd
from geopy.distance import geodesic
import os

REFERENCE_COORDS = (0.0, 0.0)

input_path = input("Enter path to input Excel file: ").strip()
output_path = input("Enter path for output Excel file: ").strip()

df = pd.read_excel(input_path, sheet_name="Sheet1")

df = df.dropna(subset=["latitude", "longitude"])

def compute_distance(row):
    point = (row["latitude"], row["longitude"])
    return geodesic(REFERENCE_COORDS, point).kilometers

df["distance_km"] = df.apply(compute_distance, axis=1)

df.to_excel(output_path, index=False)

print("✅ Done. File saved as:")
print(os.path.abspath(output_path))
