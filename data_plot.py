from __future__ import print_function
import os
import pandas as pd
import datetime as dt
import av_data
import stocks
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pf_reader
import numpy as np
# O problema de Owned é que pode ser pra aparecer as info das ações no grafico ou pra plotar desde que comprei.
# Mas nem sei se essa function vai plotar os dados mesmo


def my_stocks_get(pf, years=None, months=None, days=None, owned=None):
    """
    Gets a dict with dataframes for every stock, also used to guarantee all stock data csv were saved.
    """
    symb_list = [symb for symb in pf]
    stock_data = dict()
    for symb in symb_list:
        df = stock_get(symb, years=years, months=months, days=days, owned=owned)
        df = df.loc[df.index.hour == 18]      # Gets only daily values
        stock_data[symb] = df
    return stock_data


def stock_get(symb, years=None, months=None, days=None, owned=None):
    """
    Fetches and organize data for a stock individually in a time span.
    If no years, months, days given, all-time data will be plotted.
    Years, months and days are cummulative.
    Parameters:
    symb(str): Symbol of the stock to be plotted.
    years(int): Number of years to be plotted (goes backwards).
    months(int): Number of months to be plotted.
    days(int): Number of days to be plotted.
    owned(PORTFOLIO DICTIONARY): If any shows data since this stock was first bought, overrule others.
    """
    here = os.getcwd()
    path = here + f'\\stocks_data\\{symb}.csv'
    if not os.path.exists(path):
        # Import hist_save and call hist_save for the stock.
        av_data.av_data_get([symb])
    stockdata = pd.read_csv(path, index_col=0)
    # Changes index to proper datetime
    stockdata.index = pd.to_datetime(stockdata.index)
    stockdata = remove_zeroes(stockdata)

    tday = dt.date.today()
    delta = dt.timedelta(days=0)
    if years:
        yeardelta = dt.timedelta(days=years*365)
        delta += yeardelta
    if months:
        monthdelta = dt.timedelta(days=months*30)
        delta += monthdelta
    if days:
        daydelta = dt.timedelta(days=days)
        delta += daydelta
    if not delta or owned:
        if not delta:
            begin = stockdata.index[0].date()
        if owned:
            if symb in owned:
                order_dates = list(owned[symb].orders.keys())
                order_dates = [dt.datetime.strptime(item, '%d/%m/%Y') for item in order_dates]
                order_dates.sort()
                begin = order_dates[0].date()
    else:
        begin = tday - delta

    last_date = stockdata.index[-1].date()
    if begin <= last_date:
        return stockdata.loc[begin:tday]
    else:
        raise Exception(f'Timespan not valid for {delta.days} days.')


def format_date(x, pos=None):
    """
    Formats from a numbered index to a date string.
    Auxiliary in the task of not plotting days which there are no data for.
    """
    if isinstance(x, int):
        return data.iloc[x].name.strftime('%Y-%m-%d')
    else:
        for index, number in enumerate(data_exes):
            if x == number:
                return data['4. close'].index[index].strftime('%Y-%m-%d')


def time_to_frac(date):
    """
    System to 'weight' indexes. Every closing/opening hour is an integer, mid-day stock ticks are floats.
    Weighted from 8am to 18pm in UTC-3.
    """
    strtime = dt.time.strftime(date.time(), r'%H.%M')
    pond_ind = (10.0 - float(strtime))/8 + 1
    return -pond_ind


def index_find(df, date):
    """
    Auxiliary function to translate from numbered index to date-string.
    """
    date = dt.datetime.strptime(date, '%d/%m/%Y').date()
    for num, dfdate in enumerate(df.index):
        if dfdate.date() == date and dfdate.time() == dt.time(18, 0):
            return num
    else:
        return None


def remove_zeroes(df):
    """ Adjust zeroes for close and low values (common bugs from API)"""
    bugged_indexes = df.loc[df['4. close'] == 0].index
    for index in bugged_indexes:
        df.loc[index]['4. close'] = df.loc[index]['2. high']
        df.loc[index]['3. low'] = df.loc[index]['2. high']
    return df


def plot_stock(symb, years=None, months=None, days=None, owned=None, detail=None, tosave=None):
    """
    From dataframe, shares it globally so other functions can access, finds its length and then create a vector
    indexed from 0 to length. This is so that format_date can 'normalize' the vector in evenly spaced
    xticks and then rename it as the dates available in the dataframe, ignoring then all weekends and/or holidays when
    plotting.
    If detail is set to True, annotations from buying/selling stocks will appear on graph.
    Parameters:
    symb(str): Symbol of the stock to be plotted.
    years(int): Number of years to be plotted (goes backwards).
    months(int): Number of months to be plotted.
    days(int): Number of days to be plotted.
    owned(PORTFOLIO DICTIONARY): If any shows data since this stock was first bought, overrule others.
    detail(PORTFOLIO DICTIONARY): If any shows when orders of each stock were made in-graph.
    tosave(Bool): if True, saves figure into /Figures.
    """
    global data
    data = stock_get(symb, years=years, months=months, days=days, owned=owned)
    # Changes index to datetimes
    data.index = pd.to_datetime(data.index)
    # Fetches owned stocks
    # Gets dict with {order_date: [[qty, price, owner, Buy(T)/Sell(F)]] (array of array)} (ALL ARE STRINGS)
    if detail:
        if symb in detail:
            ords = detail[symb].orders

    # 'Weighted' indexes, to guarantee in graph a constant space between closing values dates. And to place
    # intraday in between.
    i = 1
    global data_exes
    compare = data.index[0]
    for dateobj in data.index:
        if dateobj.day != compare.day:
            i += 1
        if dateobj.time() == dt.time(18, 0):
            data_exes.append(i)
        else:
            data_exes.append(i + time_to_frac(dateobj))
        compare = dateobj

    # Colorscheme
    c1 = '#22d1ee'
    c2 = '#278ea5'
    c3 = '#1f4287'
    c4 = '#071e3d'
    c5 = '#0b3060'
    purch = '#83e85a'
    sell = '#ff304f'

    fig, ax = plt.subplots(1, 1, figsize=(8, 4))
    ax.plot(data_exes, data['4. close'], color=c1)
    ax.set_facecolor(c5)
    fig.set_facecolor(c4)

    # Gets buy/sell annotations on graph
    if detail:
        try:
            for ordate in ords:
                for order in ords[ordate]:
                    plot_index = index_find(data, ordate)
                    for i, n in enumerate(data_exes):
                        if plot_index == i:
                            bbox = dict(boxstyle='round', alpha=0.35, edgecolor=c2, fc=c2)
                            if order[3] == 'True':      # string of True/False
                                ax.plot(data_exes[i], float(order[1]), marker='o', color=purch)
                                plt.annotate(f'+{order[0]} por {order[1]}', (data_exes[i], float(order[1])),
                                             xytext=(10, -3), textcoords='offset pixels',
                                             color='w', bbox=bbox)
                            else:
                                ax.plot(data_exes[i], float(order[1]), marker='o', color=sell)
                                plt.annotate(f'-{order[0]} por {order[1]}', (data_exes[i], float(order[1])),
                                             xytext=(10, -3), textcoords='offset pixels',
                                             color='w', bbox=bbox)
        except NameError:
            raise Exception('You do not seem to have the stock being plotted.')

    # Sets minimum number of major x ticks. 12 seems to be the max that does not make graph too crowded
    day_finish = [point for point in data_exes if isinstance(point, int)]   # Ints in data_exes means tick point == 18h
    if len(day_finish) > 12:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(data_exes[-1] // 12))
    else:
        try:
            ax.xaxis.set_major_locator(ticker.MultipleLocator(data_exes[-1] // len(day_finish)))
        except:
            raise Exception('Timespan not valid for short periods.')
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))     # Changes the ticks into date strings
    ax.set_title(f'{symb}', color='w')
    plt.ylabel('Preço (R$)', color='w')
    ax.tick_params(labelcolor='white', color=c2)
    for spine in ax.spines:     # Sets graph outline to color
        ax.spines[spine].set_color(c2)
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()
    if tosave:
        here = os.getcwd()
        path = here + r'\Figures'
        if not os.path.exists(path):
            os.makedirs('Figures')
        plt.title('')
        plt.ylabel('')
        fig.savefig(f'{path}\\{symb}.png', facecolor='#071e3d')
        plt.close(fig)
        plt.close('all')
        data_exes = []  # resets data_exes so you can plot multiple times in a row


def plot_bundle(pf, years=None, months=None, days=None, owned=None, detail=None):
    symb_list = [symb for symb in pf]
    tday = dt.date.today()
    # Como organizar a carteira? Simplesmente assumo q essas mesmas ações eu sempre tive e ploto pro passado?
    # Conto o dia que cada ação foi comprada e vou calculando a percentagem?
    # todo create this
    pass


def plot_portfolio(pf, tosave=None):
    """
    Plots pie chart of a portfolio, which is organized in a dict(symb_string = STOCK_OBJECT,...).
    Investment calculated based on the number of stocks and its last closing price.
    tosave: if True, saves figure into /Figures.
    """
    symbols = []
    investments = []
    colors = ['#845ec2', '#d65db1', '#ff6f91', '#ff9671', '#ffc75f', '#f9f871', '#0089ba',
              '#008f7a', '#ff6998', '#ff847d', '#ff847d', '#ffa967', '#ffd15f', '#f9f871']
    for stock_symb in pf:
        if pf[stock_symb].qty > 0:
            symbols.append(stock_symb)
            stock_data = stock_get(stock_symb, months=1)       # Making sure to get closing value of last available day
            closing_data = stock_data.loc[stock_data.index.hour == 18]  # gets only closing values as dataframe
            closing_value = closing_data['4. close'][-1]
            stock_investment = closing_value*pf[stock_symb].qty     # Multiply qty of stock by its last closing price
            investments.append(stock_investment)
    sorted_symbols = [symb for value, symb in sorted(zip(investments, symbols))]
    fig = plt.figure()
    fig.patch.set_facecolor('#071e3d')
    sorted_investments = sorted(investments)
    plt.title(f'Investimento em Ações\n Total: R$ {sum(investments):,}0', color='w')
    plt.pie(sorted_investments, labels=sorted_symbols,
            wedgeprops={'edgecolor': 'w', 'linewidth': 1.25},
            textprops=dict(color='w'),
            colors=colors[len(investments)-1::-1])   # len used to order color scheme decently
    plt.tight_layout()
    # plt.show()
    if tosave:
        here = os.getcwd()
        path = here + r'\Figures'
        if not os.path.exists(path):
            os.makedirs('Figures')
        # plt.title('')
        fig.savefig(f'{path}\\portfolio.png', facecolor='#071e3d')
        plt.close(fig)
        plt.close('all')


data = 0
data_exes = []

port = stocks.get_portfolio(pf_reader.read_transactions('M_info.xls', 'M'))       # gets my portfolio
# dataf = stock_get('B3SA3', owned=port)
# plot_stock('JBSS3', owned=port, detail=port)
# plot_stock('B3SA3', owned=port, detail=port)
# plot_portfolio(port)

# plot_stock('EVEN3', days=10)
