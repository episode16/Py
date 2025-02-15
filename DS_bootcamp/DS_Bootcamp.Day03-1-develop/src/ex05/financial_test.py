import os
import time
import sys
import requests
import re
from bs4 import BeautifulSoup
import pytest
from unittest.mock import patch, MagicMock


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

    def process(
        self,
    ):
        try:
            if len(sys.argv) != 3:
                raise Exception("Args error. Please provide both ticker and field.")

            ticker = sys.argv[1].upper()
            field = sys.argv[2].title()

            time.sleep(5)

            parser_instance = Parser(ticker, field)
            data = parser_instance.get_data()

            print(data)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


@pytest.fixture
def test_get_soup_success():
    parser = Parser("AAPL", "Total Revenue")

    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html></html>"  # имитация html-контента
        mock_get.return_value = mock_response

        soup = parser.get_soup()
        assert soup is not None
        assert mock_get.called
        assert soup.prettify() == "<html></html>"


def test_get_soup_failure():
    parser = Parser("AAPL", "Total Revenue")

    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with pytest.raises(Exception):
            parser.get_soup()


def test_get_soup_invalid_ticker():
    parser = Parser("INVALID_TICKER", "Total Revenue")

    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with pytest.raises(Exception):
            parser.get_soup()


# Тестируем функцию find_row_div_by_title
def test_find_row_div_by_title_found():
    parser = Parser("AAPL", "Total Revenue")
    mock_soup = MagicMock()
    row_div = MagicMock()
    row_div.find.return_value = "mocked_value"
    mock_soup.find_all.return_value = [row_div]

    result = parser.find_row_div_by_title(mock_soup, "Total Revenue")
    assert result is row_div


def test_find_row_div_by_title_not_found():
    parser = Parser("AAPL", "Total Revenue")
    mock_soup = MagicMock()
    mock_soup.find_all.return_value = []

    result = parser.find_row_div_by_title(mock_soup, "Invalid Title")
    assert result is None


def test_find_row_div_by_title_empty_soup():
    parser = Parser("AAPL", "Total Revenue")
    mock_soup = MagicMock()
    mock_soup.find_all.return_value = []

    result = parser.find_row_div_by_title(mock_soup, "Some Title")
    assert result is None


# Тестируем функцию create_info
def test_create_info_success():
    parser = Parser("AAPL", "Total Revenue")
    mock_row_soup = MagicMock()
    mock_row_soup.find_all.return_value = [
        MagicMock(get_text=MagicMock(return_value="Value 1")),
        MagicMock(get_text=MagicMock(return_value="Value 2")),
    ]

    result = parser.create_info(mock_row_soup)
    assert isinstance(result, tuple)
    assert result == ("Value 1", "Value 2")


def test_create_info_empty():
    parser = Parser("AAPL", "Total Revenue")
    mock_row_soup = MagicMock()
    mock_row_soup.find_all.return_value = []

    result = parser.create_info(mock_row_soup)
    assert isinstance(result, tuple)
    assert result == ()


def test_create_info_with_non_empty_elements():
    parser = Parser("AAPL", "Total Revenue")
    mock_row_soup = MagicMock()
    mock_row_soup.find_all.return_value = [
        MagicMock(get_text=MagicMock(return_value="Test"))
    ]

    result = parser.create_info(mock_row_soup)
    assert result == ("Test",)


# Тестируем функцию get_data
def test_get_data_success():
    parser = Parser("AAPL", "Total Revenue")

    with patch.object(parser, "get_soup") as mock_get_soup, patch.object(
        parser, "find_row_div_by_title"
    ) as mock_find_row_div_by_title, patch.object(
        parser, "create_info"
    ) as mock_create_info:

        mock_get_soup.return_value = MagicMock()
        mock_find_row_div_by_title.return_value = MagicMock()
        mock_create_info.return_value = ("Mocked Data",)

        result = parser.get_data()

        assert result == ("Mocked Data",)


def test_get_data_no_field_found():
    parser = Parser("AAPL", "Non-Existing Field")

    with patch.object(parser, "get_soup") as mock_get_soup, patch.object(
        parser, "find_row_div_by_title"
    ) as mock_find_row_div_by_title:

        mock_get_soup.return_value = MagicMock()
        mock_find_row_div_by_title.return_value = None

        with pytest.raises(SystemExit):
            parser.get_data()


def test_get_data_invalid_ticker():
    parser = Parser("INVALID_TICKER", "Total Revenue")

    with patch.object(parser, "get_soup") as mock_get_soup:
        mock_get_soup.side_effect = Exception("HTTP Status Code: 404")

        with pytest.raises(SystemExit):
            parser.get_data()
