from __future__ import print_function
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import datetime as dt
import data_plot
import os
import stocks
import numpy as np
import pf_reader


def get_qty(pf, symb, start_date):
    """From a portfolio get all previously owned stock from a starting date.
    start_date has to be a datetime.datetime obj"""
    qty = 0
    for date in pf[symb].orders.keys():
        date_obj = dt.datetime.strptime(date, '%d/%m/%Y') + dt.timedelta(hours=18)    # Market closes at 18
        if (start_date - date_obj).total_seconds() > 0:
            for transaction in pf[symb].orders[date]:   # orders[date] is list of list, for multiple orders in same day
                if transaction[3] == 'True':
                    qty += int(transaction[0])
                else:
                    qty -= int(transaction[0])
    return qty


def day_orders(pf, symb, date):
    """From a date, find all orders of a certain stock in that day. Date as date datetime.datetime obj.
    If possible returns list of list with orders as list of [qty, price, owner, type] all being strings
    else returns None"""
    date_str = date.strftime('%d/%m/%Y')
    if date_str in pf[symb].orders.keys():
        return pf[symb].orders[date_str]
    else:
        return None


def find_oldest(pf):
    """ Finds oldest purchase in a portfolio"""
    date = dt.date.today()
    stock = ""
    for symb in pf:
        for date_str in pf[symb].orders:
            date_obj = dt.datetime.strptime(date_str, '%d/%m/%Y').date()
            if date_obj < date:
                date = date_obj
                stock = symb
    return date, stock


def get_rentab(pf, years=None, months=None, days=None, owned=None):
    """
    Returns a dictionary of {stock_symb: rentability vector} and the date list.
    pf: Portfolio dictionary from stocks.py.
    years(int): Number of years to be plotted (goes backwards).
    months(int): Number of months to be plotted.
    days(int): Number of days to be plotted.
    owned(PORTFOLIO DICTIONARY): If any shows data since this stock was first bought, overrule others.

    """
    def get_worth(portfolio, dfs, date):
        pf_worth = 0
        for symb in portfolio:
            stock_qty = get_qty(pf, symb, date)
            # todo testar com close, ver se da merda
            if stock_qty:
                stock_price = dfs[symb].loc[date]['1. open']
                pf_worth += stock_qty * stock_price
        return pf_worth

    # Store to print it as graph title
    global call
    if years:
        call[0] = years
    if months:
        call[1] = months
    if days:
        call[2] = days

    symb_list = [symb for symb in pf]
    stock_data = dict()

    # Guarantee to plot since first entered stock market.
    request_period = call[0]*365 + call[1]*30 + call[2]     # function time input in days
    request_period = dt.timedelta(days=request_period)
    oldest_date, oldest_stock = find_oldest(pf)
    tday = dt.date.today()
    if request_period > (tday - oldest_date):
        years = None
        months = None
        days = (tday - oldest_date).days
        print('You had no stocks back then. Plotting since first stock was purchased.')
    if owned is not None:
        years, months, days = None, None, None

    for symb in symb_list:
        data = data_plot.stock_get(symb, years=years, months=months, days=days, owned=owned)
        data = data.loc[data.index.hour == 18]      # Gets only daily values
        stock_data[symb] = data
    dates = [date for date in stock_data[oldest_stock].index]  # Gets dates from one stock, which is same for all

    rentab = []
    patrimony = []
    movement = []

    for date in dates:
        now_worth = get_worth(pf, stock_data, date)
        patrimony.append(now_worth)
        if len(movement) == 0:      # base case, first day both lists are equal and rentability is zero
            movement.append(now_worth)
        buffer = 0
        for symb in symb_list:
            orders = day_orders(pf, symb, date)
            if orders is not None:
                for order in orders:
                    if order[3] == 'True':
                        buffer += float(order[1]) * float(order[0])
                    else:
                        buffer -= float(order[1]) * float(order[0])
        movement.append(movement[-1] + buffer)
    for i in range(len(patrimony)):
        if movement[i] == 0:
            rentab.append(1)
        else:
            rentab.append(patrimony[i]/movement[i])
    return rentab, dates


def plot_rentab(ren, date_list, tosave=None):
    def format_date(x, pos=None):
        """
        Formats from a numbered index to a date string.
        Auxiliary in the task of not plotting days which there are no data for.
        """
        n = len(date_list)
        x = np.clip(int(x + 0.5), 0, n - 1)
        return date_list[x].strftime('%d/%m/%y')

    # # Separates as numered index, so all dates have the same space in-between
    exes = [i for i in range(len(date_list))]
    # Transforms rentab to percentages
    ren = np.array(ren)
    ren = (ren - 1) * 100

    # Colorscheme
    c1 = '#22d1ee'
    c2 = '#278ea5'
    c3 = '#1f4287'
    c4 = '#071e3d'
    c5 = '#0b3060'

    fig, ax = plt.subplots(1, 1, figsize=(8, 4))
    ax.axhline(y=0, color=c3)
    ax.plot(exes, ren, color=c1)
    ax.set_facecolor(c5)
    fig.set_facecolor(c4)
    ax.set_xlim(left=0)
    if call[0] or call[1] or call[2]:
        ax.set_title(f'Lucro do Portfolio em \n {call[0]} ano(s), {call[1]} mês(es), {call[2]} dia(s)', color='w')
    else:
        ax.set_title(f'Lucro do Portfolio em \n {call[0]} ano(s), {call[1]} mês(es), {len(exes)} dia(s)', color='w')
    ax.set_ylabel('Rendimento', color='w')
    ax.yaxis.set_major_formatter(ticker.PercentFormatter())
    if len(date_list) <= 10:    # Guarantee not to have more xticks than points
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    ax.tick_params(labelcolor='white', color=c2)
    for spine in ax.spines:     # Sets graph outline to color
        ax.spines[spine].set_color(c2)
    fig.autofmt_xdate()
    plt.tight_layout()
    if tosave:
        here = os.getcwd()
        path = here + r'\Figures'
        if not os.path.exists(path):
            os.makedirs('Figures')
        # ax.set_ylabel('')
        # ax.set_title('')
        fig.savefig(f'{path}\\rentability.png', facecolor=c4)
        plt.close()


call = [0, 0, 0]
port = stocks.get_portfolio(pf_reader.read_transactions('M_info.xls', 'M'))
r, d = get_rentab(port, owned=port)
plot_rentab(r, d)
