import os

# Build the path to records.txt relative to this script's location
file_path = os.path.join(os.path.dirname(__file__), "data", "records.txt")

with open(file_path) as f:
    print(f.read())