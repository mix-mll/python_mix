install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pre-commit install

lint:
	pre-commit run --all
