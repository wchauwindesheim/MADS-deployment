import requests
from pathlib import Path
from loguru import logger


def download(url, datafile: Path):
    datadir = datafile.parent
    if not datadir.exists():
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
    