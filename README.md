# Análise de Portfolio na B3
Projeto para análise de ações individuais ou portfólios utilizando o API Alpha Vantage, além de envio 
automático de email com informações pertinentes à rentabilidade.

## Pré-Requisitos
Instalando módulo do Alpha Vantage

```
pip install alpha_vantage
```
Necessário Pandas 0.25.3
```
pip install pandas==0.25.3
```
Também Matplotlib
```
pip install matplotlib
```

Adquira uma chave grátis para o uso do API [neste site](https://www.alphavantage.co/support/#api-key).

Este projeto é baseado nas informações oferecidas pelo site oficial da [CEI](cei.b3.com.br). 
Para obter as suas informações de compra e venda de ativos realize o login, siga em EXTRATO E INFORMATIVOS, NEGOCIAÇÃO DE ATIVOS,
selecione preferencialmente o período máximo de seus investimentos e exporte como arquívo EXCEL.

## Modo de uso
Adicione a chave do API como argumento key="" na função TimeSeries em av_data.py.
Preferencialmente salve o InfoCEI.xls no mesmo diretório dos outros arquivos.

Para começar com análises um método é seguir por dashboard.py:

Para criar seu portfolio, criando um OWNER_NAME_stocks.csv com todas suas transações:
```
pf = stocks.get_portfolio(pf_reader.read_transactions(EXCEL_FILE_PATH, OWNER_NAME))
```

Obtendo um pie-chart com suas ações atuais e valor atual do portfolio:
```
data_plot.plot_portfolio(pf)
```


