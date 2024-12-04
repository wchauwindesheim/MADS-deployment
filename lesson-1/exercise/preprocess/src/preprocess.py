from pathlib import Path
from loguru import logger
datadir = Path('data/raw').resolve()
datadir.exists()

from pandas import json_normalize
import json

datafile = datadir / 'posts.json'
with datafile.open() as f:
    df = json_normalize(json.load(f)["posts"], sep="_")

from datetime import datetime
import pandas as pd
import re

def bin_time(time):
    if time < datetime(2017, 12, 1):
        return 0
    elif time < datetime(2018, 1, 1):
        return 1
    elif time < datetime(2018, 8, 10):
        return 2
    elif time < datetime(2019, 8, 1):
        return 3
    else:
        return 4

def remove_url(text):
    return re.sub(r'^https?:\/\/.*[\r\n]*', '', text)

df["time"] = df["post_metadata_time"].apply(pd.to_datetime, unit="s")
df["bintime"] = df["time"].apply(lambda x : bin_time(x))
df["text"] = df["text"].apply(lambda x : str(x).replace("\n", " "))
df["text"] = df["text"].apply(lambda x : remove_url(x))
df["text"] = df["text"].apply(lambda x : x.lower())
df['size'] = df['text'].apply(lambda x : len(str(x)))
df = df[df["size"] > 50]
df.reset_index(inplace=True, drop=True)

processeddir = Path("data/processed").resolve()
if not processeddir.exists():
    logger.info(f"Creating directory {processeddir}")
    processeddir.mkdir(parents=True)
outputfile = processeddir / Path("posts.parquet")
df.to_parquet(outputfile)