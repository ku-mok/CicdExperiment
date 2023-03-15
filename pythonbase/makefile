.PHONY: lint format typecheck test
format:
	poetry run black --line-length=120 --target-version=py38 .
lint:
	poetry run flake8 --max-line-length=120
typecheck:
	poetry run mypy --ignore-missing-imports --strict --show-error-codes --show-column-numbers --show-error-context --show-traceback --pretty .
test:
	poetry run pytest 