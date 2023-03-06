# Codility

## Installation

You have to have the following tools installed prior initializing the project:

- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

### Create virtualenv

```bash
pyenv virtualenv-delete --force codility
pyenv install 3.11 --skip-existing
pyenv virtualenv `pyenv latest 3.11` codility
pyenv local codility
pyenv activate codility
```

### Install requirements (linters, pytest)

Install requirements
```bash
pip install -r requirements.txt
```

### Install linter for your commits messages

```bash
gitlint install-hook
```

## How to check code style

Fix imports:
```bash
isort .
```

Check all:
```bash
bash style.sh
```

## Run tests

```bash
pytest
```
