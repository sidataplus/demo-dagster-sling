# How to create this repository

This document describes how to create this repository step by step for reproducibility.

## Requirements

- Python v3.9 or higher
- Poetry v1.7 or higher [(Installation guide with pipx)](https://python-poetry.org/docs/#installing-with-pipx)
- Sling v1.0 or higher [(Installation guide)](https://docs.slingdata.io/sling-cli/getting-started#installation)

## Steps

1. Create a new directory with `mkdir demo-dagster-sling`
2. Run `poetry init` and fill in the details, we should have a `pyproject.toml` file now
3. Add Dagster to Poetry, following this [guide](https://docs.dagster.io/getting-started/install#installing-dagster-using-poetry)

```{bash}
poetry add dagster dagster-webserver dagster-embedded-elt
```

Install `dagster-embedded-elt` v0.21.10 will also install `sling` ^v1.0.0.`

As of 2023-11-30, `urllib3` ^v2.0 is not supported by `dagster`. We need to pin it to v1.26.15 by

```{bash}
poetry add urllib3==1.26.15 requests-toolbelt==0.10.1
```

4. Create folder `pipeline` to contain Dagster specifications.

- `__init__.py` is an entry point for Dagster to find the pipeline
- `resources.py` contains the database connection
- `assets.py` contains the data assets to be extracted and loaded

5. Register the directory `pipeline` in `pyproject.toml` for Dagster

```
[tool.dagster]
module_name = "pipeline"
```

6. Run Dagster with

```{bash}
poetry run dagster dev
```

7. Explore the Dagster UI at http://localhost:3000
