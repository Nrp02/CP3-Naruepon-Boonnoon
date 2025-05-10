from country_currency_map import COUNTRY_CURRENCY

class CountryContext:
    def __init__(self, home_country: str, dest_country: str):
        self.home_country = home_country.strip().lower()
        self.dest_country = dest_country.strip().lower()

        if self.home_country not in COUNTRY_CURRENCY:
            raise ValueError(f"Invalid home country: {self.home_country}")
        if self.dest_country not in COUNTRY_CURRENCY:
            raise ValueError(f"Invalid destination country: {self.dest_country}")

        self.base = COUNTRY_CURRENCY[self.home_country]
        self.target = COUNTRY_CURRENCY[self.dest_country]
