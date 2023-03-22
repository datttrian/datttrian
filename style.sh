set -xe
isort binary_gap/*.py --check-only
flake8 binary_gap/*.py --show-source
pylint binary_gap/*.py
mypy binary_gap/*.py
