install-python:
	uv python install

install:
	python -m venv .venv
	. .venv/bin/activate && uv pip install --all-extras --requirement pyproject.toml && pip install ipykernel && python -m ipykernel install --user --name=smart-fit-recs --display-name "Python (smart-fit-recs)"

feature-engineering:
	uv run ipython notebooks/computing_features.ipynb