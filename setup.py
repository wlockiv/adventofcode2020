from setuptools import setup, find_packages

setup(
    name='adventofcode2020',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': ['aoc2020 = adventofcode2020.cli:cli']
    },
    python_requires='>=3.8'
)
