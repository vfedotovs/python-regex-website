.DEFAULT_GOAL := help

.PHONY: test

help:  ## 💬 This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ##  Performs env setup 
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv --version
	uv venv
	uv pip install -r src/requirements.txt
	uv pip install pytest
	uv pip install pylint
	uv pip install pdoc

lint: ##  Lint code with pylint
	uv run pylint src/

test: ##  Unit tests for app
	uv run pytest -v

cov: ##  Tests coverage for app
	uv run pytest --cov src/


build: ##  Build docker container
	docker build -t vfedotovsdocker/python-regex-website:latest .	

run: ##  Run docker container locally
	docker run -p 5000:5000 vfedotovsdocker/python-regex-website

push: ##  Push container to dockerhub
	docker push vfedotovsdocker/python-regex-website

docs: ##  Generate code documentation with pdoc
	uv run pdoc src/

clean: ##  clean test files
	@rm -rf .coverage 
	@rm -rf .pytest_cache
	@rm -rf test/__pycache__/
	@rm -rf src/__pycache__/



