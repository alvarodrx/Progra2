#!/usr/bin/env python

from setuptools import setup
setup(name='kakuro',
      version='1.0.0',
      description='Library to represent and solve Kakuro puzzles.',
      author='Sebastian Raaphorst',
      author_email='srcoding@gmail.com',
      url='http://www.site.uottawa.ca/~mraap046',
      packages=['kakuro'],
      long_description="""
A package to represent adn solve Kakuro puzzles. Puzzles are input as two
dimensional arrays of either Blank objects (entries to be filled in or that are
already filled in with a value) or Block objects (greyed out entries, possibly
specifying a vertical and / or horizontal sum).

The package uses an iterative process to refine the board, and backtracking by
branching on an entry with the fewest number of possible values when refinement
fails to make any progress.

A generator is used to provide solutions in the case of boards with no solutions
or ambiguous boards with multiple solutions.""",
      classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Games/Entertainment :: Board Games',
        'Topic :: Games/Entertainment :: Puzzle Games',
        ],
      keywords='kakuro sudoku board games puzzles',
      license='Apache 2.0'
      )
