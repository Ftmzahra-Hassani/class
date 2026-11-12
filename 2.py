import pandas as pd
from pathlib import Path

# Find dataset
PROJECT_DIR = Path(file).resolve().parent.parent

FILE_PATH = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "global_temperature.csv"
)

# Read NASA dataset
df = pd.read_csv(FILE_PATH, skiprows=1)

# Display first rows
print("First five rows:")
print(df.head())

# Display dataset information
print("\nDataset information:")
df.info()

# Display column names
print("\nColumns:")
print(df.columns.tolist())

# Display dataset dimensions
print("\nDataset shape:")
print(df.shape)
