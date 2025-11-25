class Portfolio:
    def __init__(self):
        # Dictionary with ticker symbol as key and quantity as value
        self.holdings = {}

    def add_stock(self, ticker, quantity):
        if ticker in self.holdings:
            self.holdings[ticker] += quantity
        else:
            self.holdings[ticker] = quantity

    def remove_stock(self, ticker):
        if ticker in self.holdings:
            del self.holdings[ticker]

    def get_holdings(self):
        return self.holdings

    def update_quantity(self, ticker, new_quantity):
        if ticker in self.holdings:
            self.holdings[ticker] = new_quantity