import requests
from datetime import datetime, timedelta
from country_context import CountryContext

class ExchangeAnalyzer:
    API_BASE = "https://api.frankfurter.app"

    def __init__(self, context: CountryContext, days: int = 7):
        self.context = context
        self.base = context.base
        self.target = context.target
        self.days = days
        self.history = []

    def get_latest_rate(self):

        try:
            url = f"{self.API_BASE}/latest?from={self.base}&to={self.target}"
            response = requests.get(url)
            data = response.json()
            return data["rates"].get(self.target)
        except Exception as e:
            print(f"Error fetching latest rate: {e}")
            return None

    def calculate_conversion(self, amount: float, fee_percent: float):
        rate = self.get_latest_rate()
        if rate is None:
            print("Cannot get exchange rate.")
            return

        usable_amount = amount * (1 - fee_percent)
        converted = usable_amount * rate

        print(f"\nExchange Rate: 1 {self.base} = {rate} {self.target}")
        print(f"Original: {amount} {self.base}")
        print(f"After fee ({fee_percent * 100}%): {usable_amount} {self.base}")
        print(f"You will receive ≈ {converted} {self.target}")

    def get_rate_on(self, date: str):

        try:
            url = f"{self.API_BASE}/{date}?from={self.base}&to={self.target}"
            response = requests.get(url)
            data = response.json()
            return data["rates"].get(self.target)
        except Exception as e:
            print(f"Error on {date}: {e}")
            return None

    def fetch_history(self):

        self.history.clear()
        print(f"\nExchange Rate History: {self.base} → {self.target} (Last {self.days} Days)\n")
        for i in range(self.days):
            date = (datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d')
            rate = self.get_rate_on(date)
            if rate:
                print(f"{date} : {rate} {self.target}")
                self.history.append(rate)

    def analyze_trend(self):

        if len(self.history) < 2:
            print("Not enough data to analyze trend.")
            return

        avg = sum(self.history) / len(self.history)
        diff = self.history[0] - self.history[-1]
        print(f"\nAverage rate: {avg}")
        print(f"Change from oldest to newest: {diff}")