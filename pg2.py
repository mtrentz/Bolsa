from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='MGD0H8ECIQCPHG96', output_format='pandas')

msg = 'Thank you for using Alpha Vantage! Our standard API call frequency ' \
      'is 5 calls per minute and 500 calls per day. ' \
      'Please visit https://www.alphavantage.co/premium/ ' \
      'if you would like to target a higher API call frequency.'
msg2 = 'Invalid API call. Please retry or visit the documentation ' \
       '(https://www.alphavantage.co/documentation/) ' \
       'for TIME_SERIES_DAILY_ADJUSTED.'
try:
    daily_data, daily_meta_data = ts.get_daily_adjusted(symbol=f'BSDf.SA', outputsize='full')
    daily_data, daily_meta_data = ts.get_daily_adjusted(symbol=f'PETR4.SA', outputsize='full')
    daily_data, daily_meta_data = ts.get_daily_adjusted(symbol=f'PETR4.SA', outputsize='full')
    daily_data, daily_meta_data = ts.get_daily_adjusted(symbol=f'PETR4.SA', outputsize='full')
except Exception as e:
    if str(e) == msg2:
        print('Invalid API call or invalid stock symbol.')
    if str(e) == msg:
        print('Too many calls')


# daily_data, daily_meta_data = ts.get_daily_adjusted(symbol=f'SDC4.SA', outputsize='full')
