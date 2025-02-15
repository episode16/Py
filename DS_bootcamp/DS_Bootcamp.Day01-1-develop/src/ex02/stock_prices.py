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

def stocks(company_name):
    company_name = company_name.title()
    if company_name in COMPANIES:
        res = COMPANIES[company_name]
        print(STOCKS[res])
    else:
        print("Unknown company")

if len(sys.argv) == 2:
    stocks(sys.argv[1])
elif len(sys.argv) == 1:
    input_name = input("")
    stocks(input_name)
