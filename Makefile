.DEFAULT_GOAL := help

help:  ## 💬 This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

test: ##  Unit tests for app
	pytest -v

cov: ##  Tests coverage for app
	pytest --cov src/

docs: ##  Generate code documentation with pdoc
	pdoc src/

lint: ##  Lint code with pylint
	pylint src/

build: ##  Build docker container
	docker build -t flask-regex-app .

run: ##  Run docker container locally
	docker run -p 5000:5000 flask-regex-app
