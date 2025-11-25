import yfinance as yf

def fetch_live_prices(tickers):
    # Fetch latest closing prices of tickers as a Pandas Series
    data = yf.download(tickers, period='1d', interval='1d')
    prices = data['Close'].iloc[-1]
    return prices.to_dict()