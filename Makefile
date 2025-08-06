install-python:
	uv python install

install:
	python -m venv .venv
	. .venv/bin/activate && uv pip install --all-extras --requirement pyproject.toml && pip install ipykernel && python -m ipykernel install --user --name=smart-fit-recs --display-name "Python (smart-fit-recs)"

feature-engineering:
	uv run ipython notebooks/computing_features.ipynb

train-retrieval:
	uv run ipython notebooks/training_retrieval_model.ipynb

train-ranking:
	uv run ipython notebooks/training_ranking_model.ipynb
