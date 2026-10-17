import csv

class ExchangeRates:

    def __init__(self, csv_file_path):
      #opening the csv file and reading the exchange rate from it
        with open(csv_file_path, 'r') as csv_file:      
    
            reader = csv.DictReader(csv_file)      
#creation of variable to store the latest exchange rate which I will use later on. None is used to denote no specific value 'for now'
            latest_rate = None
#loop will go through each row and it will contain only the last value of the row FXAUSDCAD
            for row in reader:
                latest_rate = row["FXAUSDCAD"]
#since its a string, I will convert it to a float and store it in the variable exchange_rate
            self.exchange_rate = float(latest_rate)
   #implementation method to convert the amount from one currency to another based on the exchange rate
    def convert(self, amount, from_currency, to_currency):
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.exchange_rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.exchange_rate
   
        
#creating an instance of the ExchangeRates class and passing the path to the CSV file containing the exchange rates
rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
#accomodating the decimals of the currency exchange value
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (USD or CAD): ")
to_currency = input("Enter the currency to convert to (USD or CAD): ")

result = rates.convert(amount, from_currency, to_currency)


#print(rates.exchange_rate) - these are each of the print statements that I used to test the code and see if it was working correctly. I commented them out because they are not needed in the final version of the code.
#print(rates.convert(100, "USD", "CAD")) same as above
#print(rates.convert(100, "CAD", "USD")) same as above
print(f"${result:.2f} {to_currency}")
        


    