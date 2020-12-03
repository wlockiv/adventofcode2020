from importlib import import_module
from os import path

import click


# noinspection PyUnresolvedReferences
@click.command()
@click.argument('day', type=click.IntRange(1, 25))
@click.argument('part', type=click.Choice(['a', 'b']))
@click.pass_context
def cli(ctx, day, part):
    """Executes an AdventOfCode2020 solution 🎅

    DAY is the day of the challenge (1-25).
    PART is the challenge part (a or b).
    """
    challenge = f'day{str(day).zfill(2)}{part}'

    try:
        solution = import_module(
            f'.solutions.day{str(day).zfill(2)}{part}',
            f'adventofcode2020')

        if path.isfile(f'./inputs/{challenge}.txt'):
            with open(f'./inputs/{challenge}.txt') as input_file:
                solution.main(input_file)
        elif path.isfile(f'./inputs/{challenge[:-1]}a.txt') and part == 'b':
            click.echo('Could not find an input file for part "b". Using part "a".')
            with open(f'./inputs/{challenge[:-1]}a.txt') as input_file:
                solution.main(input_file)
        else:
            raise FileNotFoundError(f'Could not find the expected input file: {challenge}.txt')

    except ModuleNotFoundError as e:
        click.echo('The module for this day does not exist.')
        click.echo(f'Make sure a module named {challenge}.py has been add to solutions.')
        ctx.abort()
    except FileNotFoundError as e:
        click.echo(e)
        ctx.abort()
