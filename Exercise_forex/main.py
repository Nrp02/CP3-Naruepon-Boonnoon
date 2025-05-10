from exchange_analyzer import ExchangeAnalyzer
from country_context import CountryContext

home_currency = "thailand"
dest_currency = "japan"
amount = 4000000
fee_input = 0
fee = float(fee_input) / 100 if fee_input == 0 else 0.025

context = CountryContext(home_currency, dest_currency)
analyzer = ExchangeAnalyzer(context)
analyzer.calculate_conversion(amount, fee)
analyzer.fetch_history()
analyzer.analyze_trend()