#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2020-12-16
# Language: Python3

################################### IMPORTS ####################################

# Standard library
import argparse  # Used to read command line arguments.
import json  # Used to load the stock database.


# External imports
# Your imports from other packages go here


# Internal imports
from investment.stock import Stock  # Used to describe the initial market.
from investment.investor import Investor  # Used to optimize the investment.
from investment.plotter import (
    plot_investment_curve,
)  # Used to display the investment graph.

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def main():
    """
    Main function to start the command line interface and draw the desired
    investment plot.
    """

    ############################################################################
    # Parsing Command Line Arguments

    # First, we read the command line arguments.
    parser = argparse.ArgumentParser(
        description=(
            "This tool draws a plot of the ROI on the stock market after one "
            "year. It needs to be provided with a range for the initial "
            "investment as well as a stock database. See the README for more "
            "documentation."
        )
    )
    # Adding  arguments to specify the minimum and maximum investments to
    # consider.
    parser.add_argument(
        "start", type=float, help="The minimum investment to consider."
    )
    parser.add_argument(
        "stop", type=float, help="The maximum investment to consider."
    )
    # Adding an argument to specify where the database of Stocks should be
    # found.
    parser.add_argument(
        "--stock_database",
        dest="stock_database",
        default="stock_database.json",
        help="Path to the database of investments available on the market.",
    )
    # Adding an option to run the script without creating the plot, usefull for
    # testing purposes.
    parser.add_argument(
        "--no_plot",
        dest="should_plot",
        action="store_false",
        help="If set, the tool will run without saving its plot.",
    )
    # Parsing the input given by the user.
    args = parser.parse_args()

    # Getting the minimum and maximum investments from the user input.
    minimum_investment = args.start
    maximum_investment = args.stop

    # Remembering if the plot should be saved at the end or not.
    should_plot = args.should_plot

    # Sanity check
    assert minimum_investment < maximum_investment


    ############################################################################
    # Reading Stock Database

    # Getting the available stocks from the specified database. The call will
    # fail if there is no database file available.
    with open(args.stock_database, "r") as database_file:
        # First, we read all the serialized dictionaries from the database.
        all_stocks_dictionaries = json.load(database_file)
    # Then we deserialize those dictionaries into Stock objects.
    stocks = [
        Stock.fromDict(stock_dictionary)
        for stock_dictionary in all_stocks_dictionaries
    ]
    # Finally, we create the Investor object corresponding to the stock market
    # for those Stocks. This Investor will be used to optimize the Portfolios.
    investor = Investor(stocks)


    ############################################################################
    # Computing Optimal Portfolios

    # We create the lists of initial investments and associated portfolios for
    # the plot.
    investments = list()
    portfolios = list()

    # We run 100 simulations uniformly distributed between the minimum and
    # maximum investments and save each result.
    for i in range(100):
        considered_investment = minimum_investment + i / 100 * (
            maximum_investment - minimum_investment
        )
        # We compute the optimal portfolio for the considered investment.
        optimal_portfolio = investor.solve(considered_investment)

        # We add the investment and the portfolio to the lists to prepare the
        # plot.
        investments.append(considered_investment)
        portfolios.append(optimal_portfolio)


    ############################################################################
    # Drawing Expected Plot

    # We skip this section if the user asked to not save the plot.
    if should_plot:
        # Finally, we save the expected plot.
        plot_investment_curve(investments, portfolios)
        # A short feedback message for the end user.
        print("Investment curve has been saved to InvestmentPlot.png")


##################################### MAIN #####################################

if __name__ == "__main__":
    # When this file is called as a script, run the main function.
    main()

##################################### EOF ######################################
