#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2020-12-16
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from setuptools import setup  # Used to build the python package.


# External imports
# Your imports from other packages go here


# Internal imports
# Your imports within this package go here

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def main():
    """
    Calls the setup function and defines the python package.
    """
    # The setup function is used to describe the Python package that we want to
    # build.
    setup(
        name="investment",
        version="0.0.1",
        author="roadelou",
        author_email="",
        packages=["investment"], # The list of directories for the source code.
        license="GPL3",
        install_requires=["matplotlib"], # Dependencies for the package.
        python_requires=">=3.6",    # Required python version.
        entry_points="""
        [console_scripts]
        investment=investment.main:main
        """, # Create a script called investment which starts the main function
        # found in investment/main.py.
    )


##################################### MAIN #####################################

if __name__ == "__main__":
    # Start the main function when this script is called from the command line.
    main()

##################################### EOF ######################################
