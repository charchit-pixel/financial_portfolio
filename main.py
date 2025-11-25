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