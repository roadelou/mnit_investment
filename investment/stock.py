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


class Stock:
    """
    An instance of this class represents a single stock, with a price and an
    expected ROI (Return On Investment).
    """

    def __init__(self, price, roi, company):
        """
        Constructor of the Stock class.

        Arguments
        =========
         - price: A float, the price to buy the stock.
         - roi: A float, the expected return on investment for the stock after
           one year.
         - company: The name of the company emitting the action.

        Exceptions
        ==========
        This call will raise an AssertionError if the price is non-positive.
        """
        # Sanity check
        assert price >= 0

        # Storing the argument values.
        self.price = price
        self.roi = roi
        self.company = company

    @classmethod
    def fromDict(cls, dictionary):
        """
        Creates a new Stock instance from a dictionary with compatible fields,
        this is used to read a Stock from a JSON file.

        Arguments
        ========
         - dictionary: The dictionary from which the Stock object should be
            created. It should define a "price", "roi" and "company" fields.

        Returns
        =======
        The built Stock instance.

        Exceptions
        ==========
        If the argument dictionary is missing an important piece of information,
        a KeyError will be raised.
        Exceptions from the Stock constructor can also be raised.
        """
        return Stock(
            price=dictionary["price"],
            roi=dictionary["roi"],
            company=dictionary["company"],
        )

    def __repr__(self):
        """
        String representation of the Stock.
        """
        return self.company


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
