.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

dev:
	docker-compose up -d
	docker-compose exec dotbak pip install -r requirements-dev.txt
	docker-compose exec dotbak python setup.py develop
	docker-compose exec dotbak /bin/bash

virtualenv:
	virtualenv --prompt '|> dotbak <| ' env
	env/bin/pip install -r requirements-dev.txt
	env/bin/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo

test: comply
	python -m pytest \
		-v \
		--cov=dotbak \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

comply: comply-ruff comply-typing

comply-ruff:
	ruff check ./dotbak/

comply-typing:
	python -m mypy --config-file pyproject.toml -p dotbak

docker: clean
	docker build -t datafolklabs/dotbak:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
