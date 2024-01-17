Fibonacci Retracement Tool for Cryptocurrency Analysis
This Python project implements a Fibonacci Retracement tool for analyzing cryptocurrency prices. It uses historical price data to calculate key Fibonacci levels, which are often considered significant indicators for resistance and support levels in financial markets. This tool is particularly useful for traders and investors who use technical analysis to make informed decisions in the cryptocurrency market.

Features
Cryptocurrency Ticker Input: Allows users to input any cryptocurrency ticker available on Yahoo Finance (e.g., BTC-USD).
Time Frame Selection: Users can specify the time frame for the analysis (e.g., 1 year, 1 month, 5 days).
Automatic Data Retrieval: Retrieves historical data for the specified cryptocurrency from Yahoo Finance.
Fibonacci Level Calculation: Calculates key Fibonacci retracement levels based on historical price extremes (minimum and maximum closing prices).
Support and Resistance Identification: Identifies major resistance and support levels using a rolling window method.
Visualization: Plots the closing prices, Fibonacci levels, and support/resistance levels on a graph for easy visualization and analysis.

Requirements
Python 3
Libraries: matplotlib, yfinance, pandas

Installation
To use this tool, ensure you have Python 3 installed. Install the required libraries using pip:
bash
Copy code
pip install matplotlib yfinance pandas

Usage
Run the script in a Python environment. Input the desired cryptocurrency ticker and the time frame when prompted:
java
Copy code
Enter the cryptocurrency ticker (e.g., BTC-USD): BTC-USD
Enter the time frame (e.g., 1y, 1mo, 5d): 1y
The script will download the necessary data and display a plot with the cryptocurrency's closing prices, Fibonacci retracement levels, and identified support and resistance levels.

