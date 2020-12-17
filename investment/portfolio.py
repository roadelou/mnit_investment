#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2020-12-16
# Language: Python3

################################### IMPORTS ####################################

# Standard library
# Your imports from the standard library go here


# External imports
# Your imports from other packages go here


# Internal imports
# Your imports within this package go here

################################### CLASSES ####################################


class Portfolio:
    """
    A Portfolio is a set of Stock considered together.
    """

    def __init__(self, stocks):
        """
        Constructor of the Portfolio class.

        Arguments
        =========
         - stocks: An iterable of the stocks considered for this Portfolio.
        """
        # Storing the stocks as a list.
        self.stocks = list(stocks)
        # Computing the total price of the Portfolio.
        self.price = sum(stock.price for stock in self.stocks)
        # Computing the total Return On Investment (ROI) of the Portfolio.
        self.roi = sum(stock.roi for stock in self.stocks)

    def __repr__(self):
        """
        String representation of the Portfolio.
        """
        return repr(self.stocks)


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
