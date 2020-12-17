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
import matplotlib.pyplot as plt  # Used to create the plot.


# Internal imports
from investment.portfolio import Portfolio  # Hold the data for the plot.

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def plot_investment_curve(investments, portfolios):
    """
    Draws and saves the investment curve from the provided data.

    Arguments
    =========
     - The list of proposed investment amounts.
     - The list of Portfolios associated with the the proposed investments.

    Side-effects
    ============
    Save the expected figure to the file "InvestmentPlot.png".
    """
    # We first draw the return on investment of the portfolios.
    (roi_line,) = plt.plot(
        investments, [portfolio.roi for portfolio in portfolios], "r"
    )
    # We then draw the actual cost of each portfolio.
    (price_line,) = plt.plot(
        investments, [portfolio.price for portfolio in portfolios], "b"
    )
    # And finally the reference of the initial investment available.
    (initial_investment_line,) = plt.plot(investments, investments, "g")
    # We add a legend to our graph.
    plt.legend(
        [initial_investment_line, roi_line, price_line],
        [
            "Initial Investment Available",
            "Return On Investment",
            "Actual Price Of Portfolio",
        ],
    )
    # We add a title to our graph.
    plt.title(
        "Projected ROI after 1 year in the stock market based on initial investment"
    )
    # We label the axis.
    plt.xlabel("Initial Investment Available (M$)")
    # We finally save the expected plot.
    plt.savefig("InvestmentPlot.png")


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
