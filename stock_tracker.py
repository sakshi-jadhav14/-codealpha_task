# stock_tracker.py
# Simple Stock Portfolio Tracker
# - Hardcoded prices dictionary
# - User enters stock symbols and quantities
# - Program calculates per-stock value and total investment
# - Optionally saves portfolio summary to a text file

def stock_tracker():
    # Hardcoded dictionary of stock prices (you can change prices here)
    prices = {
        "AAPL": 180,   # Apple
        "TSLA": 250,   # Tesla
        "MSFT": 300,   # Microsoft
        "GOOG": 2800,  # Google
        "AMZN": 3500   # Amazon
    }

    total_investment = 0
    portfolio = []  # store strings like "AAPL: 2 shares worth $360"

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(prices.keys()))
    print("Type 'done' when finished.\n")

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper().strip()

        # finish condition
        if stock == "DONE":
            break

        # check existence
        if stock not in prices:
            print("Stock not found in dictionary. Try again (check spelling or use an available symbol).")
            continue

        # get quantity
        qty_input = input(f"Enter quantity of {stock}: ").strip()
        if not qty_input.isdigit():
            print("Please enter a valid whole number for quantity (e.g., 1, 2, 10).")
            continue

        quantity = int(qty_input)
        if quantity <= 0:
            print("Quantity must be greater than zero. Try again.")
            continue

        # calculate value and update
        value = prices[stock] * quantity
        total_investment += value
        portfolio.append((stock, quantity, value))

        print(f"Added {quantity} share(s) of {stock} worth ${value}\n")

    # summary
    print("\n----- Portfolio Summary -----")
    if not portfolio:
        print("No stocks were entered.")
    else:
        for stock, qty, val in portfolio:
            print(f"{stock}: {qty} share(s) worth ${val}")
        print(f"\nTotal Investment: ${total_investment}")

    # ask to save to file
    if portfolio:
        save = input("\nWould you like to save this summary to 'portfolio_summary.txt'? (y/n): ").strip().lower()
        if save in ("y", "yes"):
            try:
                with open("portfolio_summary.txt", "w") as f:
                    f.write("Portfolio Summary\n")
                    f.write("-----------------\n")
                    for stock, qty, val in portfolio:
                        f.write(f"{stock}: {qty} share(s) worth ${val}\n")
                    f.write(f"\nTotal Investment: ${total_investment}\n")
                print("Summary saved to 'portfolio_summary.txt'.")
            except Exception as e:
                print("Error saving file:", e)

if __name__ == "__main__":
    stock_tracker()