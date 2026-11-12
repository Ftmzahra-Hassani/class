from pathlib import Path
from urllib.request import urlopen

# NASA dataset URL
DATA_URL = (
    "https://data.giss.nasa.gov/gistemp/"
    "tabledata_v4/GLB.Ts+dSST.csv"
)

# Project directory
PROJECT_DIR = Path(file).resolve().parent.parent

# Save location
DATA_DIR = PROJECT_DIR / "data" / "raw"
FILE_PATH = DATA_DIR / "global_temperature.csv"


def download_dataset():

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading NASA climate dataset...")

    try:
        with urlopen(DATA_URL, timeout=30) as response:
            content = response.read()

        # Check downloaded content
        if len(content) < 1000:
            raise ValueError("Downloaded file is too small.")

        if b"Year,Jan,Feb" not in content:
            raise ValueError("Downloaded file format is invalid.")

        # Save dataset
        FILE_PATH.write_bytes(content)

        print("Download completed successfully!")
        print(f"Saved file: {FILE_PATH}")

    except Exception as error:
        print("Download failed!")
        print("Error:", error)


if name == "main":
    download_dataset()
