# Data Selector

> Tool to select or filter data of different types and in multiple dimensions.

[![version](https://img.shields.io/github/v/release/okp4/data-selector?style=for-the-badge&logo=github)](https://github.com/okp4/data-selector/releases)
[![lint](https://img.shields.io/github/actions/workflow/status/okp4/data-selector/lint.yml?branch=main&label=lint&style=for-the-badge&logo=github)](https://github.com/okp4/data-selector/actions/workflows/lint.yml)
[![build](https://img.shields.io/github/actions/workflow/status/okp4/data-selector/build.yml?branch=main&label=build&style=for-the-badge&logo=github)](https://github.com/okp4/data-selector/actions/workflows/build.yml)
[![test](https://img.shields.io/github/actions/workflow/status/okp4/data-selector/test.yml?branch=main&label=test&style=for-the-badge&logo=github)](https://github.com/okp4/data-selector/actions/workflows/test.yml)
[![codecov](https://img.shields.io/codecov/c/github/okp4/data-selector?style=for-the-badge&logo=codecov)](https://codecov.io/gh/okp4/data-selector)
[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=for-the-badge&logo=conventionalcommits)](https://conventionalcommits.org)
[![contributor covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=for-the-badge)](https://github.com/okp4/.github/blob/main/CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=for-the-badge)](https://opensource.org/licenses/BSD-3-Clause)

## Purpose

The `Data Selector` tool allows you to select a sample of the dataset, specifying a number of rows. It is possible to delete or keep columns. Another parameter allows the selection of data in a column according to its value(s).

The output result is saved in a `.csv` file.

## Usage

The usage is given as follows:

```sh
Usage: data-selector [OPTIONS] COMMAND [ARGS]...

  Data selection interactive tool.

Options:
  --help  Show this message and exit.

Commands:
  selector  Tool to select Data to Keep/Delete
  version   Print the application version information
```

To use the command to select data in file:

```sh
Usage: data-selector selector [OPTIONS]

  Tool to select Data to Keep/Delete

Options:
  -i, --input FILE                Data file to convert  [required]
  -out, --output TEXT             name for the output files  [required]
  -f, --force                     Overwrite existing files
  -s, --file_sep TEXT             File separator (csv).
  -row, --nb_rows INTEGER         Number of rows to import from input_file.
  -keep, --columns_to_keep FILE   Path to file with columns to keep.
  -delete, --columns_to_delete FILE
                                  Path to file with columns to delete.
  -values, --values_to_keep FILE  Path to file with columns and data to keep.
  --help                          Show this message and exit.
```

### Specification for json parameter files

For the -keep and the `-delete` option, the template is given below :

```json
[
"<column#1>",
"<column#2>",
"<column#3>",
"<column#4>",
"<column#5>"
]
```

**column#x** are the columns you want to select/delete.
**Note that you can add as many columns as needed.**

For the `values` option, the template is given below :

```json
{  
  "<column#1>":["<value#1>", "<value#2"],    
  "<column#2>":["<value#1>", "<value#2", "<value#3", "<value#4"],  
  "<column#3>":["<value#1>"]   
}
```

**column#x** are the columns you want to select/delete.
**value** is a list of the values you want to keep on this column.
**Note that you can add as many columns as needed.**

### Build & run docker image (locally)

Build a local docker image using the following command line:

```sh
docker build -t data-selector .
```

Once built, you can run the container locally with the following command line:

```sh
docker run -ti --rm -v <your_path>:/DATA data-selector selector -i DATA/<path_to_data> -out DATA/<out_name> -s <file_sep> -keep DATA/<path_to_select_columns> -delete DATA/<path_to_delete_columns> -values DATA/<path_to_select_data_columns>
```

-v allows to mount a volume and to use your local data on the docker environment.

**your_path**: Local directory where the data (data to be selected, and parameter json files) are stored

**path_to_data**: The name of the file to select data from (in the Directory).

**out_name**: The name you want to give to the output file.

**file_sep**: File separator of the input file.

**path_to_select_columns**: Path towards json parametrization file.

**path_to_delete_columns**: Path towards json parametrization file.

**path_to_select_data_columns**: Path towards json parametrization file.

## Build

Project is built by [poetry](https://python-poetry.org).

```sh
poetry install
```

## Lint

### Python linting

> ⚠️ Be sure to write code compliant with linters or else you'll be rejected by the CI.
**Code linting** is performed by [flake8](https://flake8.pycqa.org).

```sh
poetry run flake8 --count --show-source --statistics
```

**Static type check** is performed by [mypy](http://mypy-lang.org/).

```sh
poetry run mypy .
```

## Unit Test

> ⚠️ Be sure to write tests that succeed or else you'll be rejected by the CI.
Unit tests are performed by the [pytest](https://docs.pytest.org) testing framework.

```sh
poetry run pytest -v
```

## You want to get involved? 😍

Please check out OKP4 health files :

- [Contributing](https://github.com/okp4/.github/blob/main/CONTRIBUTING.md)
- [Code of conduct](https://github.com/okp4/.github/blob/main/CODE_OF_CONDUCT.md)
