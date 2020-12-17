#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2020-12-17
# Language: Python3

################################### IMPORTS ####################################

# Standard library
# Your imports from the standard library go here


# External imports
# Your imports from other packages go here


# Internal imports
from investment import (
    Stock,
    Portfolio,
    Investor,
)  # The classes used to run the tests

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def prepare_investor():
    """
    Helper function which returns an Investor on which tests can be performed.
    """
    # Creating a few sample Stocks.
    stocks = [Stock(price=i, roi=2 * i, company=str(i)) for i in range(10)]
    # Returning an investor built for this market.
    return Investor(stocks)


def test_portfolio():
    """
    Simple test to verify that the properties of a Portfolio (price, roi) are
    correctly computed.
    """
    # Creating a few stocks.
    stocks = [Stock(price=i, roi=2 * i, company=str(i)) for i in range(10)]
    # Creating a Portfolio for all those stocks.
    portfolio = Portfolio(stocks)
    # Asserting that the price of the Portfolio is computed correctly.
    assert portfolio.price == sum(stock.price for stock in stocks)
    # Asserting that the roi of the Portfolio is computed correctly.
    assert portfolio.roi == sum(stock.roi for stock in stocks)


def test_investor():
    """
    Simple test to verify that the Investor solves the optimization correctly.
    """
    # First, we get the prepared Investor.
    investor = prepare_investor()
    # Then, we test that it returns the expected ROI for several known scenarii.
    assert investor.solve(0).roi == 0
    assert investor.solve(1).roi == 2
    assert investor.solve(5).roi == 10
    assert investor.solve(13).roi == 26


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
