import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

# Function to calculate Fibonacci Retracement levels
def fibonacci_retracement_levels(price_min, price_max):
    levels = {
        '23.6%': price_max - 0.236 * (price_max - price_min),
        '38.2%': price_max - 0.382 * (price_max - price_min),
        '50.0%': price_max - 0.5 * (price_max - price_min),
        '61.8%': price_max - 0.618 * (price_max - price_min),
        '100.0%': price_min
    }
    return levels

# Identify major resistance and support levels
def find_support_resistance(data):
    highs = data['High'].rolling(window=15).max()
    lows = data['Low'].rolling(window=15).min()
    return highs, lows

# Ask user for the cryptocurrency ticker and the time frame
ticker = input("Enter the cryptocurrency ticker (e.g., BTC-USD): ")
period = input("Enter the time frame (e.g., 1y, 1mo, 5d): ")

# Download historical data for the specified cryptocurrency
data = yf.download(ticker, period=period)

# Calculate Fibonacci Retracement levels
price_min = data['Close'].min()
price_max = data['Close'].max()
fib_levels = fibonacci_retracement_levels(price_min, price_max)

# Identify support and resistance levels
resistance_levels, support_levels = find_support_resistance(data)

# Plot the data along with Fibonacci levels and support/resistance levels
plt.figure(figsize=(12, 8))
plt.title(f'Fibonacci Retracement Levels for {ticker}')
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.plot(data['Close'], label='Close Price', color='blue')

# Plot Fibonacci levels
for level, price in fib_levels.items():
    plt.axhline(y=price, linestyle='--', label=f'Fib {level} ({price:.2f})')

# Plot major resistance and support levels
plt.plot(resistance_levels, label='Resistance', linestyle='-', color='red')
plt.plot(support_levels, label='Support', linestyle='-', color='green')

plt.legend()
plt.show()
