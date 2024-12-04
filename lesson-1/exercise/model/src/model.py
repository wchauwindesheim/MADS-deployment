import numpy as np
from loguru import logger
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import manhattan_distances
import os
import seaborn as sns
import matplotlib.pyplot as plt


log_dir = "/app/logs"
log_file = os.path.join(log_dir, "model.log")

# Add a file handler to Loguru
logger.add(log_file, rotation="10 MB")  # Rotate the log file after it reaches 10 MB

class TextClustering:
    def __init__(self):
        self.vectorizer = CountVectorizer(analyzer="char", ngram_range=(3, 3))
        self.n = 0

    def __call__(
        self, text: list[str], k: int, batch: bool, method: str = "PCA"
    ) -> np.ndarray:
        if batch:
            text = self.batch_seq(text, k)
        distance = self.fit(text)
        X = self.reduce_dims(distance, method)
        return X

    def batch_seq(self, text: list[str], k: int) -> list[str]:
        longseq = " ".join(text)
        self.n = int(len(longseq) / k)
        logger.info(f"Splitting text into {k} parts of {self.n} characters each")
        parts = [longseq[i : i + self.n] for i in range(0, len(longseq), self.n)]
        if len(parts) > k:
            logger.info(f"Removing {len(parts) - k} parts")
            parts = parts[:k]
        return parts

    def get_labels(self, df) -> np.ndarray:
        assert self.n > 0, "First create clusters"
        df.loc[:, "group"] = df["size"].cumsum() // self.n
        labels = df["post_metadata_source_site"].unique()
        mapping = {label: i for i, label in enumerate(labels)}
        df["source"] = df["post_metadata_source_site"].apply(lambda x: mapping[x])
        sourcemean = np.round(df.groupby("group").source.mean()).values.reshape(-1, 1)
        labels = sourcemean.flatten().astype(str)
        return labels

    def fit(self, parts: list[str]) -> np.ndarray:
        X = self.vectorizer.fit_transform(parts)
        X = np.asarray(X.todense())
        distance = manhattan_distances(X, X)
        return distance

    def reduce_dims(self, distance: np.ndarray, method: str = "PCA") -> np.ndarray:
        if method == "PCA":
            logger.info("Using PCA")
            model = PCA(n_components=2)
        else:
            logger.info("Using t-SNE")
            model = TSNE(n_components=2)
        X = model.fit_transform(distance)
        return X


import pandas as pd
from pathlib import Path

datadir = Path("data/processed")
if not datadir.exists():
    logger.info(f"Creating directory {datadir}")
    datadir.mkdir(parents=True)
datafile = datadir / Path("posts.parquet")
df = pd.read_parquet(datafile)

clustering = TextClustering()

import numpy as np
from io import BytesIO
k = 100
X = clustering(df["text"], k=k, batch=True, method="PCA")
labels = clustering.get_labels(df)
import seaborn as sns
plt.figure(figsize=(6, 4))
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels)
plt.title("Seaborn Scatterplot")

# Save the plot to a BytesIO object
buf = BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
plt.close()
        
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()
        self.wfile.write(buf.read())

server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
logger.info('Starting server on port 8000')
server.serve_forever()