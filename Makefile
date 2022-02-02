setup:
	python -m venv .venv && . .venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*

clean: clean-pyc clean-test

test: clean
	. .venv/bin/activate && pytest --cov=bioinformatics --cov-report=term-missing --cov-fail-under 95 --disable-pytest-warnings

lint:
	. .venv/bin/activate && pylint bioinformatics -j 4 --reports=y --fail-under=9  --ignore-patterns=test_.*?py

check: test lint