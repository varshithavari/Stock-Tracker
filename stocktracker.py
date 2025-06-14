import yfinance as yf

# Step 1: Define your stock portfolio
portfolio = {
    "AAPL": {"shares": 10, "buy_price": 150},
    "MSFT": {"shares": 5, "buy_price": 280},
    "TSLA": {"shares": 8, "buy_price": 700},
    "GOOGL": {"shares": 2, "buy_price": 2400}
}

# Step 2: Fetch live stock prices and calculate values
def track_portfolio(portfolio):
    total_invested = 0
    total_value = 0

    print(f"{'Stock':<10}{'Qty':<5}{'Buy Price':<12}{'Current Price':<15}{'P/L'}")
    print("-" * 60)

    for symbol, data in portfolio.items():
        shares = data["shares"]
        buy_price = data["buy_price"]
        current_price = yf.Ticker(symbol).history(period='1d')["Close"].iloc[-1]

        invested = shares * buy_price
        current_value = shares * current_price
        profit_loss = current_value - invested

        total_invested += invested
        total_value += current_value

        print(f"{symbol:<10}{shares:<5}{buy_price:<12}{round(current_price,2):<15}{round(profit_loss,2)}")

    print("-" * 60)
    print(f"Total Invested: ${round(total_invested,2)}")
    print(f"Current Value:  ${round(total_value,2)}")
    print(f"Overall P/L:     ${round(total_value - total_invested,2)}")

# Run the tracker
track_portfolio(portfolio)
