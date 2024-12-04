import requests
from pathlib import Path
from loguru import logger
import os

# Define the directory and file name
log_dir = "/app/logs"
log_file = os.path.join(log_dir, "app.log")

# Add a file handler to Loguru
logger.add(log_file, rotation="10 MB")  # Rotate the log file after it reaches 10 MB

def download(url, datafile: Path):
    datadir = datafile.parent
    if not datadir.exists():
        logger.info(f"Current working directory: {os.getcwd()}")
        logger.info(f"Full datadir path: {Path(datadir).resolve()}")        
        logger.info(datafile)
        logger.info(f"Creating directory {datadir}")
        logger.info(datadir)
        datadir.mkdir(parents=True)

    if not datafile.exists():
        logger.info(f"Downloading {url} to {datafile}")
        response = requests.get(url)
        with datafile.open("wb") as f:
            f.write(response.content)
    else:
        logger.info(f"File {datafile} already exists, skipping download")


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/jkingsman/JSON-QAnon/main/posts.json"
    datadir = Path("data/raw")
    datafile = datadir / Path("posts.json")
    download(url, datafile)        
    