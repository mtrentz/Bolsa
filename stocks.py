import datetime as dt
import csv
import numpy as np
import pf_reader


class Stock:
    def __init__(self, name, orders):
        self.name = name
        self.orders = orders
        self.qty = 0
        # Sums final quantity of stocks
        for day in self.orders:
            for transaction in self.orders[day]:
                if str(transaction[3]) == 'True':    # stored as string
                    self.qty += int(transaction[0])
                else:
                    self.qty -= int(transaction[0])

    def __add__(self, other):
        if self.name == other.name:
            # Checks if there is already an order in the same day
            if not set(self.orders.keys()).isdisjoint(other.orders.keys()):
                name = self.name
                # This only works if 'other' has only one date key!
                # Then it copies self.orders and changes the dict for the date which overlaps
                datekey = other.orders.keys()
                datekey = list(datekey)[0]
                neworders = self.orders
                neworders[datekey] = np.append(self.orders[datekey], other.orders[datekey], axis=0)
                return Stock(name, neworders)
            # If all orders are in different day, then it just merges dictionaries
            else:
                name = self.name
                # This merges the two dicts in a third. (python 3.5 or higher)
                orders = {**self.orders, **other.orders}
                return Stock(name, orders)
        else:
            return print('You can not add different stocks')


def get_portfolio(csv_file):
    """ Goes through stock csv made from pf_reader. Adds each stock into a dictionary of {symb = stock_obj}"""
    pf = {}
    stock_file = csv_file
    with open(stock_file, newline='') as csvfile:
        stockreader = csv.reader(filter(lambda line: line[0] != '#', csvfile))
        for row in stockreader:
            if row:
                # Creates a order dictionary, keys are dates on which orders happened. Values are an array of
                # [qty, price, owner, type(buy(T) or sell(F))
                if row[0] not in pf:
                    pf[row[0]] = Stock(row[0], {row[3]: np.array([[row[1], row[2], row[4], row[5]]])})
                else:
                    pf[row[0]] = pf[row[0]] + Stock(row[0], {row[3]: np.array([[row[1], row[2],
                                                                                row[4], row[5]]])})
    return pf
