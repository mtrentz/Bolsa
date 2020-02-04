# Análise de Portfólio na B3
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
Para obter as suas informações de compra e venda de ativos realize o login, siga em 'extrato e informativos', 
'negociação de ativos, selecione preferencialmente o período máximo de seus investimentos e exporte como arquívo excel.

## Modo de uso
Adicione a chave do API como argumento key="" na função TimeSeries em av_data.py.
Preferencialmente salve o InfoCEI.xls no mesmo diretório dos outros arquivos.

Para começar com análises seguir por dashboard.py:

Para criar seu portfolio, criando um OWNER_NAME_stocks.csv com todas suas transações:
```
pf = stocks.get_portfolio(pf_reader.read_transactions(EXCEL_FILE_PATH, OWNER_NAME))
```

Obtendo um pie-chart com suas ações atuais e valor atual do portfolio:
```
data_plot.plot_portfolio(pf)
```
<img src="https://i.imgur.com/wSfAlPT.png" alt="piechart" width="450"/>

### Calculo de Rentabilidade

Tendo criado um portfolio(pf) é possível visualizar ações individuais com comentários de compras/vendas efetuadas:
```
data_plot.stock_plot('B3SA3', owned = pf, detail = pf)
```
<img src="https://i.imgur.com/vzzYNKV.png" alt="stock_detail" width="600"/>

Sem um portfólio passando como parâmetros years, months, days como 'int' é possivel plotar progressão dos preços de uma ação
em qualquer período de tempo com:
```
data_plot.stock_plot('PETR4', years=1, months=4, days=0)
```

Já tendo o portfólio é possível calculos de rentabilidade, como exemplo aqui é feito nos ultimos seis mêses:
```
r, d, m = rentability.get_rentab(pf, months=6)

rentability.plot_rentab(r, d)
```
<img src="https://i.imgur.com/PSfeyc9.png" alt="rentab" width="600"/>

```
rentability.plot_bars(m, d)
```
<img src="https://i.imgur.com/8faF9ac.png" alt="profit" width="600"/>

### Envio de Emails

Para enviar emails automáticos por email_generator.py é necessário uma conta de e-mail com segurança reduzida. Tendo em mãos
este email, forneça as informações de login em newsletter.py.

O padrão do email mostrado aqui está em newsletter.html. As figuras a serem apresentadas são controladas por newsletter.py e
em que período de tempo e ações a serem plotadas são geradas por email_generator.py.

Exemplo de um newsletter:

<img src="https://i.imgur.com/yRIpLno.png" alt="newsletter" width="450"/>

