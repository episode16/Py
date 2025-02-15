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

def main():
    if len(sys.argv) != 2:
        return

    input_string = sys.argv[1]
    input_string = input_string.replace(' ', '')
    words = [word.strip() for word in input_string.split(',')]
    
    if ',,' in input_string:
        return

    results = []

    for word in words:
        if not word:
            continue

        word_upper = word.upper()
        word_title = word.title()

        if word_title in COMPANIES:
            ticker = COMPANIES[word_title]
            price = STOCKS.get(ticker)
            results.append(f"{word_title} stock price is {price}")
        elif word_upper in COMPANIES.values():
            company = 'unknown'
            for name, tick in COMPANIES.items():
                if tick == word_upper:
                    company = name
                    break
            results.append(f"{word_upper} is a ticker symbol for {company}")
        else:
            results.append(f"{word} is an unknown company or an unknown ticker symbol")

    print("\n".join(results))

if __name__ == "__main__":
    main()
