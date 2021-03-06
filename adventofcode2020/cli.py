import math
import time
from importlib import import_module
from os import path
from typing import Callable, IO

import click


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
@click.option('--silent-fail', is_flag=True)
def run(day, part, silent_fail):
    """Executes an AdventOfCode2020 solution.

    DAY is the day of the challenge (1-25).
    PART is the challenge part (a or b).
    """
    challenge = f'day{str(day).zfill(2)}{part}'

    try:
        solution = import_module(
            f'.solutions.day{str(day).zfill(2)}{part}',
            f'adventofcode2020').main

        if path.isfile(f'./inputs/{challenge}.txt'):
            with open(f'./inputs/{challenge}.txt') as input_file:
                call_timed(solution, input_file)
        elif path.isfile(f'./inputs/{challenge[:-1]}a.txt') and part == 'b':
            with open(f'./inputs/{challenge[:-1]}a.txt') as input_file:
                call_timed(solution, input_file)
        else:
            raise FileNotFoundError(f'Could not find the expected input file: {challenge}.txt')

    except ModuleNotFoundError:
        if silent_fail:
            raise ModuleNotFoundError
        click.echo('Error: The module for this day does not exist.')
        click.echo(f'Make sure a module named {challenge}.py has been add to solutions.')
    except FileNotFoundError as e:
        if not silent_fail:
            click.echo(e)
    except AttributeError:
        if not silent_fail:
            click.echo(
                'Error: A valid solution module must have a main() function that takes a file object as a parameter.')


@cli.command()
@click.pass_context
def run_all(ctx: click.Context):
    """Executes all Advent of Code Solutions."""
    day_range = list(range(1, 26))
    parts = ('a', 'b')

    for day in day_range:
        for part in parts:
            try:
                ctx.invoke(run, day=day, part=part, silent_fail=True)
            except ModuleNotFoundError:
                click.echo('---')
                click.echo(f'Reached the end at Day {day} Part {part.upper()}')
                exit()
