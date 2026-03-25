# AIM: To read data from a JSON file and parse nested structures into a flat table format. [cite: 247, 248]
# DESCRIPTION: JSON is a lightweight format for structured data. Pandas uses pd.read_json() for loading. [cite: 250, 251]
# Nested structures must be flattened using json_normalize() to create a tabular format. [cite: 252, 253]

import pandas as pd [cite: 255]
from pandas import json_normalize [cite: 256]
# Sample nested JSON data
data = { "students": [ 
    {"name": "Ram", "details": {"age": 20, "marks": 85}}, 
    {"name": "Sita", "details": {"age": 19, "marks": 90}}, 
    {"name": "Ravi", "details": {"age": 21, "marks": 78}} 
]} [cite: 258, 259, 261, 263, 266, 268]
# Convert JSON data into DataFrame
df = json_normalize(data["students"]) [cite: 272]
# Display the flattened DataFrame
print("Flattened DataFrame from JSON:") [cite: 274]
print(df) [cite: 274]
