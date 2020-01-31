import pf_reader
import stocks
import data_plot
import rentability
import newsletter
import matplotlib.pyplot as plt


# TODO nao tenho certeza q vai funcionar caso nao passe nenhum years etc..
def gen_mail(to_mail, excel_file, owner, years=None, months=None, days=None, owned=None, detail=None):
    # todo notar que ownede e detail aqui é bool
    # Fetching portfolio from excel file
    pf = stocks.get_portfolio(pf_reader.read_transactions(excel_file, owner))

    # Checks for owned/detail, changes to portfolio if True since it's the necessary input for other functions
    if owned:
        owned = pf
    if detail:
        detail = pf

    # Calculate rentability. r = vectors of rentability of each stock and overall, d = date list, m = money_dif list
    r, d, m = rentability.get_rentab(pf, years=years, months=1, days=days, owned=owned)

    # Plots and saves rentability graph of portfolio
    rentability.plot_rentab(r, d, tosave=True)

    # Plots and save profit bar graph
    rentability.plot_bars(m, d, tosave=True)

    # Plots and saves piechart of portfolio
    data_plot.plot_portfolio(pf, tosave=True)

    # Finds stock which varied the most up and down
    symbs = []
    variations = []
    stocks_data = data_plot.my_stocks_get(pf, years=years, months=months, days=days, owned=owned)
    for symb in stocks_data:
        symbs.append(symb)
        final = stocks_data[symb].iloc[-1]['4. close']
        first = stocks_data[symb].iloc[0]['1. open']
        variations.append(final-first)
    sorted_list = sorted(zip(variations, symbs))
    # todo posso começar a colocar as duas que mais subiram, e as duas que mais cairam etc etc...
    best = sorted_list[-1][1]   # stock symb which went the most up
    worst = sorted_list[0][1]   # stock which went down the most

    # Plots and saves stock data. # todo change owned and make it be same as months and days above
    # todo calcular com data_plot, get data (acho) qual das ações q tiveram maior variação em um certo periodo
    data_plot.plot_stock(f'{best}', years=years, months=months, days=days, owned=owned, detail=detail, tosave=True)
    data_plot.plot_stock(f'{worst}', years=years, months=months, days=days, owned=owned, detail=detail, tosave=True)

    # Sends mail
    newsletter.send_mail(to_mail, f'{best}', f'{worst}')


gen_mail('mateus.trentz@gmail.com', 'M_info.xls', 'M', owned=True, detail=True)
# gen_mail('kochhann@anfip.org.br', 'C_info.xls', 'C', owned=True, detail=True)

# todo achar um jeito de passar o timespan pras figuras, pra falar 'a que mais caiu em X dias foi...'
# todo criar meu rcparam pra mais facil editar e mudar todos os graficos
# todo grafico rentabilidade diz (1 mes) mas mostra sempre
# todo talvez forçar pra mostrar o primeiro mes nos de bar, caso tenha sido o mes que a pessoa entrou na bolsa
# pf = stocks.get_portfolio(pf_reader.read_transactions('M_info.xls', 'M'))


