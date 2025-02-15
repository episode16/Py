import os
import time
import sys
import requests
import re
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, ticker, field):
        self.ticker = ticker
        self.field = field
        self.url = (
            f"https://finance.yahoo.com/quote/{self.ticker}/financials?p={self.ticker}"
        )
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://finance.yahoo.com",
        }

    def get_soup(self):
        resp = requests.get(self.url, headers=self.headers)
        if resp.status_code != 200:
            raise Exception(f"HTTP Status Code: {resp.status_code}")
        return BeautifulSoup(resp.content, "html.parser")

    def find_row_div_by_title(self, soup, title_value):
        row_divs = soup.find_all("div", class_=re.compile(r"^row"))
        for row_div in row_divs:
            if row_div.find("div", title=title_value):
                return row_div
        return None

    def create_info(self, row_soup):
        info = tuple(
            [
                elem.get_text(strip=True)
                for elem in row_soup.find_all("div", class_=re.compile(r"^column"))
                if elem.get_text(strip=True)
            ]
        )
        return info

    def get_data(self):
        try:
            soup = self.get_soup()
            row_soup = self.find_row_div_by_title(soup, self.field)
            if row_soup is None:
                raise Exception(f"Field '{self.field}' not found on the page.")

            info = self.create_info(row_soup)
            return info

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise Exception("Args error. Please provide both ticker and field.")

        ticker = sys.argv[1].upper()
        field = sys.argv[2].title()

        # time.sleep(5)

        parser_instance = Parser(ticker, field)
        data = parser_instance.get_data()

        print(data)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
