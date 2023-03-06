set -xe
isort ./*.py --check-only
flake8 ./*.py --show-source
pylint ./*.py
mypy ./*.py
