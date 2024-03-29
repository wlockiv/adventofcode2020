from setuptools import setup, find_packages

setup(
    name='adventofcode',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',

    ],
    entry_points={
        'console_scripts': ['aoc = adventofcode.cli:cli']
    },
    python_requires='>=3.8'
)
