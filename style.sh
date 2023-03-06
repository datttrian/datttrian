set -xe
isort main --check-only
flake8 main --show-source
pylint main
mypy main
