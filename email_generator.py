import pf_reader
import stocks
import data_plot
import rentability
import newsletter
import matplotlib.pyplot as plt


def rentability_ranking(pf, years=None, months=None, days=None, owned=None):
    # Conferir pq isso subida/descida de reais, nao sei se é melhor que percentagem.
    symbs = []
    variations = []
    stocks_data = data_plot.my_stocks_get(pf, years=years, months=months, days=days, owned=owned)
    for symb in stocks_data:
        symbs.append(symb)
        final = stocks_data[symb].iloc[-1]['4. close']
        first = stocks_data[symb].iloc[0]['1. open']
        variations.append(final-first)
    sorted_list = sorted(zip(variations, symbs))
    return sorted_list


def gen_mail(to_mail, excel_file, owner, years=None, months=None, days=None, owned=None, detail=None):
    """
    Prepares all the figures to be sent as mail in newsletter.py. For that gets persons portfolio,
    rentability and finds the stocks which changed the most, up and down, in the input timespan.
    Params:
        to_mail(str): email string of recipient.
        excel_file: File path of excel document from B3 or IBOVESPA with 'transação de ativos'
        owner(str): Any tag, name or ID to identify owner of each transation in a CSV
        years, months, days(int): Cummulative timespan to plot rentability and stock data.
        detail(Bool): If true, override other timespan and plot data since the beginning of portfolio.
    """
    # todo notar que ownede e detail aqui é bool
    # Fetching portfolio from excel file
    pf = stocks.get_portfolio(pf_reader.read_transactions(excel_file, owner))

    # Checks for owned/detail, changes to portfolio if True since it's the necessary input for other functions
    if owned:
        owned = pf
    if detail:
        detail = pf

    # Calculate rentability. r = vectors of rentability of each stock and overall, d = date list, m = money_dif list
    r, d, m = rentability.get_rentab(pf, years=years, months=months, days=days, owned=owned)

    # Plots and saves rentability graph of portfolio
    rentability.plot_rentab(r, d, tosave=True)

    # Plots and save profit bar graph
    rentability.plot_bars(m, d, tosave=True)

    # Plots and saves piechart of portfolio
    data_plot.plot_portfolio(pf, tosave=True)

    # Finds stock which varied the most up and down
    sorted_list = rentability_ranking(pf, years=years, months=months, days=days, owned=owned)
    best = sorted_list[-1][1]   # stock symb which went the most up
    worst = sorted_list[0][1]   # stock which went down the most

    # Plots and saves stock data. # todo change owned and make it be same as months and days above
    # todo calcular com data_plot, get data (acho) qual das ações q tiveram maior variação em um certo periodo
    data_plot.plot_stock(f'{best}', years=years, months=months, days=days, owned=owned, detail=detail, tosave=True)
    data_plot.plot_stock(f'{worst}', years=years, months=months, days=days, owned=owned, detail=detail, tosave=True)

    # Sends mail
    newsletter.send_mail(to_mail, f'{best}', f'{worst}')


# gen_mail('mateus.trentz@gmail.com', 'M_info.xls', 'M', days=10, detail=True)
gen_mail('kochhann@anfip.org.br', 'C_info.xls', 'C', months=1, detail=True)

# todo criar meu rcparam pra mais facil editar e mudar todos os graficos
# todo lucro em reais nao aparece se o periodo é menor que o mês
# todo passar o treco de achar ação que mais e menos rendeu pra uma funcao
# pf = stocks.get_portfolio(pf_reader.read_transactions('M_info.xls', 'M'))


