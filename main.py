import os
import requests
import json
import time
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class CoinMarketCap():
    def __init__(self):
        self.url = ""
        self.headers = {}
        self.parameters = {}

    def fetch_currencies_data(self):
        response = requests.get(
            url=self.url, headers=self.headers, params=self.parameters).json()
        return response["data"]


class CryptoReport(CoinMarketCap):
    def __init__(self):
        super().__init__()
        self.url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        self.headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": os.environ.get("API_KEY")
        }
        self.reports = self.get_reports()

    def get_reports(self):
        reports = {
            "most_traded_currencies": self.most_tradedCurrency(),
            "best_ten_currencies": self.best_ten_currencies(),
            "worst_ten_currencies": self.worst_ten_currencies(),
            "amount_top_twenty_currencies": self.amount_top_twenty_currencies(),
            "amount_by_volumes_24h_currencies": self.amount_by_volumes_currencies(),
            "gain_top_twenty_currencies": self.gain_top_ten_currencies(),
        }
        return reports

    def most_tradedCurrency(self):
        # Return the cryptocurrency with the largest volume (in $) of the last 24 hours
        self.parameters = {
            "start": 1,
            "limit": 1,
            "sort": "volume_24h",
            "sort_dir": "desc",
            "convert": "USD"
        }
        currencies = self.fetch_currencies_data()
        return currencies[0]

    def best_ten_currencies(self):
        # Return the best 10 cryptocurrencies by percentage increase in the last 24 hours
        self.parameters = {
            "start": 1,
            "limit": 10,
            "sort": "percent_change_24h",
            "sort_dir": "desc",
            "convert": "USD"
        }
        currencies = self.fetch_currencies_data()
        return currencies

    def worst_ten_currencies(self):
        # Return the best 10 cryptocurrencies by percentage increase in the last 24 hours
        self.parameters = {
            "start": 1,
            "limit": 10,
            "sort": "percent_change_24h",
            "sort_dir": "asc",
            "convert": "USD"
        }
        currencies = self.fetch_currencies_data()
        return currencies

    def amount_top_twenty_currencies(self):
        # Return the amount of money required to purchase one unit of each of the top 20 cryptocurrencies in order of capitalization
        amount = 0
        self.parameters = {
            "start": 1,
            "limit": 20,
            "sort": "market_cap",
            "sort_dir": "desc",
            "convert": "USD"
        }
        currencies = self.fetch_currencies_data()
        for currency in currencies:
            if amount < currency["quote"]["USD"]["price"]:
                amount = currency["quote"]["USD"]["price"]
        return round(amount, 2)

    def amount_by_volumes_currencies(self):
        # Return the amount of money required to purchase one unit of all cryptocurrencies whose last 24-hour volume exceeds $ 76,000,000
        amount = 0
        self.parameters = {
            "start": 1,
            "limit": 100,
            "volume_24h_min": 76000000,
            "convert": "USD"
        }
        currencies = self.fetch_currencies_data()
        for currency in currencies:
            amount += currency["quote"]["USD"]["price"]
        return round(amount, 2)

    def gain_top_ten_currencies(self):
        initialAmount = 0
        todayPrice = 0
        self.parameters = {
            "start": 1,
            "limit": 20,
            "sort": "market_cap",
            "sort_dir": "desc",
            "convert": "USD"
        }
        currencies = self.fetch_currencies_data()
        for currency in currencies:
            yesterdayPrice = currency["quote"]["USD"]["price"] / \
                (1 + (currency["quote"]["USD"]["percent_change_24h"] / 100))
            todayPrice += currency["quote"]["USD"]["price"]
            initialAmount += yesterdayPrice

        gain = round((((todayPrice - initialAmount) / initialAmount) * 100), 1)
        return gain


def makeJson(report):
    # Create a json file named with the actual date into the 'Report' directory
    fileName = time.strftime("Report_%d-%m-%Y")
    pathFile = os.path.dirname(os.path.abspath(__file__))
    completeNameFile = os.path.join(pathFile, "report")
    path = os.path.join(completeNameFile, fileName)

    try:
        os.mkdir(completeNameFile)
    except OSError:
        pass  # Already exists
    with open(path, "w") as output:
        json.dump(report, output)


#  While cicle
def main():
    seconds = 60
    minutes = 60
    hours = 24

    while True:
        report = CryptoReport()

        print("------------------------------------------------------------")
        print("Crypto currencies reports of " + time.strftime("%d %B %Y:"))
        print("")

        print("Most traded currencies: " +
              report.reports["most_traded_currencies"]["symbol"])

        print("Best 10 currencies: ", end=" ")
        for currency in report.reports["best_ten_currencies"]:
            print(currency["symbol"] + ",", end=" ")

        print("")

        print("Worst 10 currencies: ", end=" ")
        for currency in report.reports["worst_ten_currencies"]:
            print(currency["symbol"] + ",", end=" ")

        print("")

        print("Amount top twenty currencies: " +
              str(report.reports["amount_top_twenty_currencies"]) + "$")

        print("Amount by volume: " +
              str(report.reports["amount_by_volumes_24h_currencies"]) + "$")

        print('Gain top 20: ' +
              str(report.reports['gain_top_twenty_currencies']) + '%')

        print("------------------------------------------------------------")
        print("👉 This project is avaible on my GitHub profile --> " +
              "https://github.com/luigilesca/python")
        print("")
        print("👉 You can find me on LinkedIn --> " +
              "https://www.linkedin.com/in/luigi-lesca/")
        print("------------------------------------------------------------")

        makeJson(report.reports)
        time.sleep(seconds * minutes * hours)


if __name__ == "__main__":
    main()
