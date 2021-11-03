# :tulip: toolip :tulip:

A collection of python utils for webapps

![Tests](https://github.com/SatelCreative/toolip/actions/workflows/tests.yml/badge.svg)

## Installation

```bash
pip install toolip
```

## Contributing

If you want to contribute a small change/feature, the best is to just create a PR with
your changes.
For bigger changes/features it's best to open an issue first and discuss it to agree
on the code organization and overall implementation before spending too much time on
the code, unless you want to keep it in your own forked repo.

### Setting up the development environment

We use the [python poetry](https://python-poetry.org/) package to manage this package.
Follow the official instructions to install poetry on your system then once you clone
this repository just just need to do the following to install the dependencies from
the development environment, as well as install `toolip` in
[editable mode](https://pip.pypa.io/en/stable/cli/pip_install/#install-editable):

```bash
poetry install
```

Then you can start monitoring the code for changes and run the test suite this way:

```bash
poetry shell
scripts/test_watch.sh
```

### Build and run documentation (lazydocs/mkdocs)

Documentation for this package is handled by `lazydocs` and so it needs a few steps to generate it locally.

Inside `poetry shell`:

```bash
lazydocs --overview-file="index.md" \
--src-base-url="https://github.com/SatelCreative/toolip/tree/main" \
--output-path="./docs/api-docs" \
--validate .

mkdocs build
mkdocs serve
```

The default URL is at `127.0.0.1:8000`.

## Maintenance

We use [poetry](https://python-poetry.org/) to manage the dependencies and
[flit](https://flit.readthedocs.io/en/latest/index.html) to build and publish to pypi
because unlike poetry it allows to set the metadata on pypi such as author or homepage.

### Howto publish

1. Change the version in the `pyproject.toml` and `toolip/__init__.py` files
   - you can use `poetry version XXXXX` to change `pyproject.toml`
2. Commit to git
3. Run `poetry build` to create the package folders in `/dist`
4. Run `flit publish` to publish to PyPI
5. Tag the release in git and push it to Github
