
import csv


class ExchangeRates:
    def __init__(self, filename):
        # Read the exchange rate data from the CSV file.
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Get the latest USD/CAD exchange rate from the last row.
        self.usd_cad_rate = float(rows[-1]["FXAUSDCAD"])

    def convert(self, amount, from_currency, to_currency):
        # Convert the amount from one currency to another.
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_cad_rate

        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.usd_cad_rate

        else:
            return amount


# Create an ExchangeRates object using the CSV file.
exchange_rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

# Prompt the user to enter the conversion details.
amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency to convert from (USD or CAD): ").upper()
to_currency = input("Enter the currency to convert to (USD or CAD): ").upper()

# Convert the amount and display the result.
converted_amount = exchange_rates.convert(amount, from_currency, to_currency)

print(f"{amount:,.2f} {from_currency} = ${converted_amount:,.2f} {to_currency}")
