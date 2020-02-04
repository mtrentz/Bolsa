import pandas as pd
import re
import csv
import datetime as dt


def read_transactions(excelfile, owner):
    """ Reads excel file from cei.b3.com.br for (Transações de Ativos) """
    # filename = owner + '_stocks.csv'
    pf_file = excelfile
    filename = owner + '_stocks.csv'

    data = pd.read_excel(pf_file, header=None)
    data = data.fillna(0)   # Replaces NaN with 0

    begin = 0
    end = 0
    todrop = []
    for row in range(data.shape[0]):
        if data.iloc[row][1] == 'Data Negócio':
            begin = row + 1
            for extra_rows in range(begin, data.shape[0]):
                if not re.match(r'^[A-Za-z0-9_-]{4}\d$', str(data.iloc[extra_rows][6])) and data.iloc[extra_rows][6] != 0:
                    todrop.append(extra_rows)
                if not re.search(r'^\s{3}\d{2}/\d{2}/\d{2}$', str(data.iloc[extra_rows][1])):
                    end = extra_rows - 1
                    break

    todrop.reverse()
    data = data.drop(todrop)
    end = end - len(todrop)

    dates = []
    types = []
    symbs = []
    qtys = []
    prices = []

    for row in range(begin, end+1):
        dates.append(data.iloc[row][1].strip())
        symbs.append(data.iloc[row][6])
        qtys.append(data.iloc[row][8])
        types.append(data.iloc[row][3].strip())
        prices.append(data.iloc[row][9])

    dates = [dt.datetime.strptime(date, '%d/%m/%y').strftime('%d/%m/%Y') for date in dates]  # Changes string format
    types = [True if order == 'C' else False for order in types]    # From C/V to True/False

    with open(filename, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        comentline = '# Nome, Qtd, Preço, Data(dd/mm/aaaa), Dono (M/C), Tipo: Compra(True) Venda(False)\n\n'
        csvfile.write(comentline)
        for i in range(len(dates)):
            filewriter.writerow([symbs[i], qtys[i], prices[i], dates[i], owner, types[i]])

    # to be used in stocks.py
    return filename
