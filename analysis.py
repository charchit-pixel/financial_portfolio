def calculate_portfolio_value(portfolio, prices):
    total_value = 0
    stock_values = {}
    for ticker, qty in portfolio.items():
        price = prices.get(ticker, 0)
        value = price * qty
        stock_values[ticker] = value
        total_value += value
    return total_value, stock_values