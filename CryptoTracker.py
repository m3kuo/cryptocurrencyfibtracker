import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

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

# Ask user for the cryptocurrency ticker, time frame, and graph type
ticker = input("Enter the cryptocurrency ticker (e.g., BTC-USD): ")
period = input("Enter the time frame (e.g., 1y, 1mo, 5d): ")
graph_type = input("Enter graph type (line/candlestick): ").lower()

# Download historical data for the specified cryptocurrency
data = yf.download(ticker, period=period)

# Calculate Fibonacci Retracement levels
price_min = data['Close'].min()
price_max = data['Close'].max()
fib_levels = fibonacci_retracement_levels(price_min, price_max)

# Identify support and resistance levels
resistance_levels, support_levels = find_support_resistance(data)

# Create Plotly figure
fig = go.Figure()

# Add the main plot (line or candlestick)
if graph_type == 'line':
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
elif graph_type == 'candlestick':
    fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='Candlestick'))

# Add Fibonacci levels
for level, price in fib_levels.items():
    fig.add_hline(y=price, line_dash="dash", annotation_text=f'Fib {level}', annotation_position="bottom right")

# Add major resistance and support levels
fig.add_trace(go.Scatter(x=resistance_levels.index, y=resistance_levels, mode='lines', name='Resistance', line=dict(color='red')))
fig.add_trace(go.Scatter(x=support_levels.index, y=support_levels, mode='lines', name='Support', line=dict(color='green')))

# Update layout
fig.update_layout(title=f'Fibonacci Retracement Levels for {ticker}', xaxis_title='Date', yaxis_title='Price in USD', legend_title="Legend")

# Show plot
fig.show()
