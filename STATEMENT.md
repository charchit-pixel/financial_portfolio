# financial-portfolio-tracker
Overview
A Python application for tracking and analyzing real-time investment portfolio performance. Users input stock symbols and quantities, fetch live prices, and view total and individual asset values using interactive charts.

Features
Add/edit/remove stocks and quantities
Fetch live market prices
Calculate total and asset-wise portfolio value
Visualize portfolio holdings using charts

Technologies/Tools Used
Python
pandas
matplotlib
yfinance (for live price data)
VS Code or any Python IDE

Steps to Install & Run the Project
Clone the repository from GitHub
Install dependencies:
pip install pandas matplotlib yfinance
Navigate to the project folder
Run the main script:
python main.py

Instructions for Testing
Add sample stocks when prompted (e.g., AAPL, MSFT, NVDA)
Enter quantities for each
Type ‘DONE’ to finish input
View portfolio calculations and charts in the console and window
Modify stock data and rerun for testing....

#The Codes for portfolio management are
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


  #The codes for data fetcher are
  import yfinance as yf

def fetch_live_prices(tickers):
    # Fetch latest closing prices of tickers as a Pandas Series
    data = yf.download(tickers, period='1d', interval='1d')
    prices = data['Close'].iloc[-1]
    return prices.to_dict()


 #The Codes for analysis are
 def calculate_portfolio_value(portfolio, prices):
    total_value = 0
    stock_values = {}
    for ticker, qty in portfolio.items():
        price = prices.get(ticker, 0)
        value = price * qty
        stock_values[ticker] = value
        total_value += value
    return total_value, stock_values

 #The Codes for data visualization are
 import matplotlib.pyplot as plt

def plot_portfolio(stock_values):
    tickers = list(stock_values.keys())
    values = list(stock_values.values())

    plt.bar(tickers, values, color='skyblue')
    plt.title('Portfolio Stock Values')
    plt.ylabel('Value in USD')
    plt.xlabel('Stock Ticker')
    plt.show()

#The Code for main are
from portfolio_management import Portfolio
from data_fetcher import fetch_live_prices
from analysis import calculate_portfolio_value
from visualization import plot_portfolio

def main():
    portfolio = Portfolio()

    print("Enter your portfolio stocks (type 'done' when finished):")
    while True:
        ticker = input("Stock ticker symbol: ").upper()
        if ticker == 'DONE':
            break
        try:
            quantity = int(input("Quantity owned: "))
            portfolio.add_stock(ticker, quantity)
        except ValueError:
            print("Please enter a valid integer quantity.")

    holdings = portfolio.get_holdings()
    if not holdings:
        print("Portfolio is empty.")
        return

    print("\nFetching live stock prices...")
    prices = fetch_live_prices(list(holdings.keys()))
    
    print("\nCurrent Stock Prices:")
    for ticker, price in prices.items():
        print(f"{ticker}: ${price:.2f}")

    total_value, stock_values = calculate_portfolio_value(holdings, prices)
    print(f"\nTotal portfolio value: ${total_value:,.2f}")

    plot_portfolio(stock_values)

if __name__ == "__main__":
    main()
