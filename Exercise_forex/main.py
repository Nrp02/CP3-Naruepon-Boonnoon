from exchange_analyzer import ExchangeAnalyzer
from country_context import CountryContext

home_currency = input("Enter your country: ").strip().lower()
dest_currency = input("Enter destination country: ").strip().lower()
amount_input = input("Enter amount in your currency: ").strip()
amount = float(amount_input) if amount_input else 0

fee_input = input("Enter transaction fee (%): ").strip()
fee = float(fee_input) / 100 if fee_input == 0 else 0.025

context = CountryContext(home_currency, dest_currency)
analyzer = ExchangeAnalyzer(context)
analyzer.calculate_conversion(amount, fee)
analyzer.fetch_history()
analyzer.analyze_trend()