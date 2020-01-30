initial_value = get_worth(pf, stock_data, dates[0])
for date in dates:
    final_value = 0
    amount_purchased = 0
    amount_sold = 0
    for symb in symb_list:
        start_qty = get_qty(pf, symb, date)
        end_qty = start_qty
        orders = day_orders(pf, symb, date)  # Find if stock was purchased that day returns None if there wasnt
        if start_qty or orders is not None:  # Gets data if stock was already owned, or bought that day
            close_price = stock_data[symb].loc[date]['4. close']
            bought = [0, 0.0]  # as [qty, amount of money]
            sold = [0, 0.0]
            if orders is not None:
                for order in orders:
                    if order[3] == 'True':
                        bought[0] += int(order[0])
                        bought[1] += float(order[1]) * float(order[0])
                    else:
                        sold[0] += int(order[0])
                        sold[1] += float(order[1]) * float(order[0])
                end_qty = start_qty + bought[0] - sold[0]
            now_worth = end_qty * close_price
            final_value += now_worth
            amount_purchased += bought[1]
            amount_sold -= sold[1]
        else:
            rentab[dates.index(date)] = 0
    rentab[dates.index(date)] = final_value / (initial_value + amount_purchased - amount_sold)
    initial_value = initial_value + amount_purchased - amount_sold

    # todo ainda ta errado pq ta dando 200% de lucro.
return rentab, dates