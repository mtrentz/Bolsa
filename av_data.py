import csv
import os
from alpha_vantage.timeseries import TimeSeries
import time
import datetime as dt
import re
import stocks
# TODO hide key
ts = TimeSeries(key='MGD0H8ECIQCPHG96', output_format='pandas')


def index_rename(index):
    """
    Receives a date-like index, adjust the time which is delayed by 2h on alpha-vantage, and adds the stock closing
    hour for daily ticks.
    """
    index = str(index)
    dre = r'\d{4}-\d{2}-\d{2} 00:00:00'
    dtre = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    tdelta = dt.timedelta(hours=2)
    tdelta18 = dt.timedelta(hours=18)
    if re.match(dre, index):
        # Adds the closing time of each 'daily' tick
        return str(dt.datetime.strptime(index, '%Y-%m-%d %H:%M:%S')+tdelta18)
    if re.match(dtre, index):
        # Fixes time of tick which is two hours behind.
        return str(dt.datetime.strptime(index, '%Y-%m-%d %H:%M:%S')+tdelta)


def av_data_get(stocklist):
    """
    Loads owned stock, fetches stock data from alpha-vantage then exports it to a csv file
    """
    # Gets stocks owned/needed
    # Guarantees no duplicate
    stock_symbs = set()
    if type(stocklist) == str:
        stock_symbs.add(stocklist)
    elif type(stocklist) == list:
        for item in stocklist:
            stock_symbs.add(item)
    here = os.getcwd()
    path = here + r'\stocks_data'
    if not os.path.exists(path):
        os.makedirs('stocks_data')
    for stock in stock_symbs:
        daily_data = []
        intraday_data = []
        for attempt in range(2):
            try:
                # Gets daily data, fixes its columns and indexes
                print(f'Fetching daily data for {stock}.')
                daily_data, daily_meta_data = ts.get_daily_adjusted(symbol=f'{stock}.SA', outputsize='full')
                daily_data = daily_data.drop(columns=['5. adjusted close',
                                                      '7. dividend amount',
                                                      '8. split coefficient'])
                daily_data = daily_data.rename(columns={'6. volume': '5. volume'})
                return daily_data
                daily_data = daily_data.rename(index=index_rename)
            # todo achar diferença entre value error de tempo e value error de nome de ação
            except:
                print("Waiting for API authorization.")
                time.sleep(65)
            else:
                break
        else:
            print(f'Unavailable daily data for {stock}')
        for attempt in range(2):
            try:
                # Gets intraday data, fixes indexes
                print(f'Fetching intraday data for {stock}. ')
                intraday_data, intraday_meta_data = ts.get_intraday(symbol=f'{stock}.SA', outputsize='full')
                intraday_data = intraday_data.rename(index=index_rename)    # Fixes starting time
            except:
                print("Waiting for API authorization.")
                time.sleep(65)
            else:
                break
        else:
            print(f'Unavailable intraday data for {stock}')
        try:
            # Put both daily and intra daily together, sort it by date and export
            print(f'Saving data for {stock}.')
            all_data = daily_data.append(intraday_data)
            all_data = all_data.sort_index()
            all_data.to_csv(os.path.join(path, f'{stock}.csv'))
        except:
            print(f'Failed getting data for {stock}.')


# owned = list(stocks.mystocks.keys())
# data = av_data_get(['ITUB3'])