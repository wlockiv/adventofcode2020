from datetime import date
import math
import re
import time
from importlib import import_module
import os
from typing import Callable, IO

import click
from click.types import DateTime

from adventofcode.util import copy_template_file


def call_timed(solution_fn: Callable, input_file: IO):
    start = time.time()
    solution_fn(input_file)
    print(f'\t⏱  :: {math.ceil((time.time() - start) * 1000)}ms')


@click.group()
def cli():
    """Advent of Code 2020 Helper 🎅"""
    pass


@cli.command()
@click.argument('day', type=click.IntRange(1, 25))
@click.argument('part', type=click.Choice(['a', 'b']))
@click.option('-y', '--year', type=click.INT, default=(date.today().year))
@click.option('--silent-fail', is_flag=True)
def run(day, part, year, silent_fail):
    """Executes an AdventOfCode2020 solution.

    YEAR is the year of the challenge (2020, 2021, etc).
    DAY is the day of the challenge (1-25).
    PART is the challenge part (a or b).
    """
    challenge = f'day{str(day).zfill(2)}{part}'

    try:
        solution = import_module(
            f'.{year}.day{str(day).zfill(2)}{part}',
            f'adventofcode').main

        input_dir = f'./inputs/{year}'
        if os.path.isfile(f'{input_dir}/{challenge}.txt'):
            with open(f'{input_dir}/{challenge}.txt') as input_file:
                call_timed(solution, input_file)
        elif os.path.isfile(f'{input_dir}/{challenge[:-1]}a.txt') and part == 'b':
            with open(f'{input_dir}/{challenge[:-1]}a.txt') as input_file:
                call_timed(solution, input_file)
        else:
            raise FileNotFoundError(
                f'Could not find the expected input file for: {year}/{challenge}.txt')

    except ModuleNotFoundError as e:
        if silent_fail:
            raise ModuleNotFoundError
        if re.search(r'adventofcode\.\d{4}\.day\d{2}[ab]', e.msg):
            click.echo('Error: The module for this day does not exist.')
            click.echo(
                f'Make sure a module named {challenge}.py has been add to solutions.')
        else:
            click.echo('ModuleNoteFoundError: ' + e.msg)
    except FileNotFoundError as e:
        if not silent_fail:
            click.echo(e)


@cli.command()
@click.pass_context
@click.option('-y', '--year', type=click.INT, default=(date.today().year))
def run_all(ctx: click.Context, year):
    """Executes all Advent of Code Solutions."""
    day_range = list(range(1, 26))
    parts = ('a', 'b')

    for day in day_range:
        for part in parts:
            try:
                ctx.invoke(run, day=day, part=part,
                           year=year, silent_fail=True)
            except ModuleNotFoundError:
                click.echo('---')
                click.echo(
                    f'Reached the end at Year {year}, Day {day}, Part {part.upper()}')
                exit()


@cli.command()
@click.argument('day', type=click.IntRange(1, 25))
@click.argument('part', type=click.Choice(['a', 'b']))
@click.option('-y', '--year', type=click.INT, default=(date.today().year))
def make(day, part, year):
    """Creates a solution file."""
    solution_destination = copy_template_file(year, day, part)

    input_destination = f'./inputs/{year}/day{str(day).zfill(2)}a.txt'
    with open(input_destination, 'a') as f:
        pass

    click.echo(
        f'The solution module and input file for Day {day}, Part {part} of {year} have been made!')
    click.echo(f'\t Solution: {solution_destination}')
    click.echo(f'\t    Input: {input_destination}')
