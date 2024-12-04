# slanggen

First, build the environment with
```bash
rye sync --all-features
```

We use `--all-features` because we also want to install the optional packages (`flask`,` beautifulsoup4`.)

Note how I added 
```toml
[[tool.rye.sources]]
name = "torch-cpu"
url = "https://download.pytorch.org/whl/cpu"
```
This makes sure that you dont download an additional 2.5GB of GPU dependencies, if you dont need them.
This can be essential in keeping the container within a manageable size.

train the model:
```bash
python src/slanggen/main.py
```
This should fill the `assets` folder with a file `straattaal.txt` and fill the `artefacts` folder with a trained model.
Check this with `ls`

If everything works as expected, you can build the `src/slanggen` package into a wheel:
```bash 
rye build --clean
```

This should produce a `dist` folder, and shoud add these two files:
```bash
❯ lsd dist
.rw-r--r--@ 9.5k username  4 Dec 14:35  slanggen-0.3.1.tar.gz
.rw-r--r--@ 6.0k username  4 Dec 14:35  slanggen-0.3.1-py3-none-any.whl
```

With this, you can now run 

```bash
python backend/app.py
```
And this will start an api at http://127.0.0.1:80
Test if everything works as expected.
