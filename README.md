# Advent of Code

## Install the CLI

```zsh
# Make a virtual environment
python3 -m venv env

# Activate the environment
source env/bin/activate

# Install to the env in editable mode
(env) pip install -e .
```

## Make a solution file

```zsh
# (With the python env activated)
(env) aoc make [OPTIONS] DAY {a|b}

Options:
  -y, --year INTEGER
```

The new solution file can be found in the `adventofcode/[year]` directory.

## Run a solution

```zsh
# (With the python env activated)
aoc run [OPTIONS] DAY PART

Options:
  -y, --year INTEGER
```

Executes an AdventOfCode solution.

`YEAR` is the year of the challenge (2020, 2021, etc). `DAY` is the day of the
challenge (1-25). `PART` is the challenge part (a or b).
