import json
import os
from pathlib import Path

import torch
from flask import Flask, jsonify, render_template, request
from loguru import logger
from slanggen import models
from tokenizers import Tokenizer
from utils import sample_n

logger.add("logs/app.log", rotation="5 MB")
frontend_folder = Path("frontend").resolve()
artefacts = Path("artefacts")

if not frontend_folder.exists():
    raise FileNotFoundError(f"Cant find the frontend folder at {frontend_folder}")
else:
    logger.info(f"Found {frontend_folder}")

if not artefacts.exists():
    raise FileNotFoundError(f"Cant find the artefacts folder at {artefacts}")
else:
    logger.info(f"Found {artefacts}")


app = Flask(
    __name__,
    template_folder=frontend_folder / "templates",
    static_folder=frontend_folder / "static",
)


def load_model():
    tokenizerfile = str(artefacts / "tokenizer.json")
    tokenizer = Tokenizer.from_file(tokenizerfile)
    with (artefacts / "config.json").open("r") as f:
        config = json.load(f)
    model = models.SlangRNN(config["model"])
    modelpath = str(artefacts / "model.pth")
    model.load_state_dict(torch.load(modelpath, weights_only=False))
    return model, tokenizer


model, tokenizer = load_model()
starred_words = []


def new_words(n, temperature):
    output_words = sample_n(
        n=n,
        model=model,
        tokenizer=tokenizer,
        max_length=20,
        temperature=temperature,
    )
    return output_words


@app.route("/generate", methods=["GET"])
def generate_words():
    try:
        n = int(request.args.get("num_words", 10))
        temperature = float(request.args.get("temperature", 1.0))
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    try:
        words = new_words(n, temperature)
        return jsonify(words)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/starred", methods=["GET", "POST"])  # type: ignore
def handle_starred_words():
    if request.method == "GET":
        return jsonify(starred_words)
    elif request.method == "POST":
        word = request.json.get("word")  # type: ignore
        if word not in starred_words:
            starred_words.append(word)
        return jsonify(starred_words)


@app.route("/unstarred", methods=["POST"])
def handle_unstarred_words():
    word = request.json.get("word")  # type: ignore
    if word in starred_words:
        starred_words.remove(word)
    return jsonify(starred_words)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 80)))
