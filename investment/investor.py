#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2020-12-16
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from itertools import combinations  # Used to build combinations of Stocks.


# External imports
# Your imports from other packages go here


# Internal imports
from investment.portfolio import (
    Portfolio,
)  # Used to compare the potential investments

################################### CLASSES ####################################


class Investor:
    """
    Class responsible for finding the best investment in the market according to
    a fixed budget.
    """

    def __init__(self, stocks):
        """
        Constructor of the Investor class.

        Arguments
        =========
         - stocks: An iterable of all the Stocks available on the market.
        """
        # Storing the list of available Stocks.
        self.stocks = list(stocks)

        # Building the list of possible Portfolios.
        self.portfolios = list()
        # We iteratively build all the possible Portfolios of a given number of
        # actions.
        for n in range(len(self.stocks)):
            # First we create all the combinations of n Stocks.
            combinations_of_n_stocks = combinations(self.stocks, n)
            # Then we add the corresponding Portfolios to our list.
            self.portfolios.extend(
                [
                    Portfolio(combination)
                    for combination in combinations_of_n_stocks
                ]
            )

    def solve(self, investment):
        """
        Finds the best Portfolio on the market for the given available
        investment.

        Arguments
        =========
         - investment: The total available investment to build the Portfolio.

        Returns
        =======
        The optimal Portfolio for the given investment.

        Exceptions
        ==========
        This call will raise an AssertionError if the investment is
        non-positive.
        """
        # Sanity check
        assert investment >= 0

        # First, we limit ourselves to Portfolios whose price fits in our
        # investment.
        filtered_portfolios = [
            portfolio
            for portfolio in self.portfolios
            if portfolio.price <= investment
        ]
        # Then, we return the remaining Portfolio with the highest return on
        # investment (ROI).
        return max(filtered_portfolios, key=lambda portfolio: portfolio.roi)


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
