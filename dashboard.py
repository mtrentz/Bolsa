import pf_reader
import stocks
import data_plot
import rentability
import newsletter
import email_generator

# To read portfolio. Excel file from https://cei.b3.com.br/CEI_Responsivo/home.aspx, 'Negociação de Ativos"
# 'M' just as a identifier of stocks/portfolio owner
pf = stocks.get_portfolio(pf_reader.read_transactions('M_info.xls', 'M'))

# Fetch rentability(r), list of dates being analyzed (d), variability in BRL of each day (m).
# if owned = pf (portfolio), then fetches all-time data of portfolio
r, d, m = rentability.get_rentab(pf, years=0, months=1, days=0, owned=None)

# Plotting rentability, profit, and pie chart of portfolio
rentability.plot_rentab(r, d)
rentability.plot_bars(m, d)
data_plot.plot_portfolio(pf)

