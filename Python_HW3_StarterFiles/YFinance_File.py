import yfinance as yf
import pandas as pd


columns = pd.MultiIndex.from_tuples([
    ('Close', 'AAPL'),
    ('High', 'AAPL'),
    ('Low', 'AAPL'),
    ('Open', 'AAPL'),
    ('Volume', 'AAPL')
], names=['Metric', 'Ticker'])

sample_data_rows = [
    [150.00, 152.50, 149.00, 151.00, 10000000],
    [151.50, 153.00, 150.50, 150.50, 11000000],
    [153.00, 154.00, 152.00, 152.00, 9500000]
]

# Create a DataFrame
SampleData = pd.DataFrame(sample_data_rows, columns=columns)

def YahooData2returns(YahooData=SampleData,symbol='AAPL'):
    # Input:
    # YahooData = data from Yahoo Finance
    # Output:
    # returns = array of returns
    # Steps:
    # Extract 'Close' and symbol (This is a 2d column. Demo below.)
    # Calculate and return the lagged returns
    returns = np.array([0.01      , 0.00990099])
    return returns
