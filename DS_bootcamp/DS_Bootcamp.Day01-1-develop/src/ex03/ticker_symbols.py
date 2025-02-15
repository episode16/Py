import sys
COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
}

STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
}

def ticker(ticker):
    ticker = ticker.upper()
    if ticker in STOCKS:
        keys = [key for key, value in COMPANIES.items() if value == ticker]
        print(", ".join(keys) + ' ' + str(STOCKS[ticker]))
    else:
        print("Unknown company")

if len(sys.argv) == 2:
    ticker(sys.argv[1])