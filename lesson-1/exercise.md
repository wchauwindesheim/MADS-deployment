# Exercise

## setup
0. setup your own project (git, dependency management, etc, see [codestyle](https://github.com/raoulg/codestyle) for details)
1. Install the dependencies using the `pyproject.toml` file.
2. Have a look at the minimal and minimal-fastapi examples.
2. Have a look at the notebooks, and run them.

Using the information from the lesson and the minimal examples, you will move this to docker.

Isolate the three steps in the process:
1. ingest
2. preprocess
3. model

This means you should set up a project that looks like this:
```bash
├── Makefile                   <- Makefile with commands like `make ingest` or `make train`
|── pyproject.toml             <- The dependencies file
├── README.md                  <- The top-level README for developers using this project.
├── logs
│   └── logfile.log            <- Logfile for the project
├── data                       <- The data directory for raw and processed data
│   ├── processed
│   └── raw
├── ingest                     <- The ingest module
│   ├── ingest.Dockerfile      <- Dockerfile for the ingest module.
│   └── ingest.py              <- The script for the ingest module
└── preprocess
    ├── preprocess.Dockerfile
    └── preprocess.py
├── model
│   ├── model.py
│   ├── requirements.txt       <- The requirements file for reproducing the analysis environment
│   ├── serve.Dockerfile
    └── serve.py
```

Please note that you will probably want to install dependencies in the ingest and preprocess
images too, but if it are just one or two dependencies,
it is reasonable to ommit the requirements file and
simply do eg. `RUN pip install --no-cache-dir pandas` to install just pandas.