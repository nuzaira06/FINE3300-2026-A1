# FINE3300-2026-A1
Finance Python Assignment 1

## Description : 
Design an exchange rate calculator - design a class that will read a file (currency exchange rate data), to convert CAD to USD and vice versa.

## Files used:
ExchangeRates.py — My original Python implementation of the exchange rate calculator.
BankOfCanadaExchangeRate.2026.csv — The CSV file containing exchange rate data from the Bank of Canada.

## Features
Reads exchange rate data from a CSV file using Python's built-in csv module.
Use the latest USD/CAD exchange rate available in the file. (FXUSDCAD)
Implements an ExchangeRates class to manage the exchange rate and currency conversions.
Converts USD to CAD by multiplying the amount by the exchange rate.
Converts CAD to USD by dividing the amount by the exchange rate.
Prompts the user to enter the amount, source currency, and destination currency.
Displays the converted amount rounded to two decimal places (float).

## 4. The main program actions
Instantiation: rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv") creates an object from the class. Passing the file path is what triggers __init__.
User input: input() prompts for the amount, the currency to convert from and the currency to convert to. The amount is cast to a float. As the assignment allows, no input validation is performed.
Calling the method: rates.convert(amount, from_currency, to_currency) uses dot notation to call the method on the object and the result is printed.


## How to run program:
Install Python and place the Python file and the CSV file in the same folder.
Open the folder in Visual Studio Code.
Open the terminal and run:python ExchangeRates.py
Enter the amount to convert, the source currency (USD or CAD), and the destination currency (USD or CAD) when prompted.

## Example of running program
To convert USD 100,000 to CAD, enter:
Amount: 100000
From currency: USD
To currency: CAD
The program calculates the converted amount using the latest exchange rate in the CSV file.

## Technology used : 
Technologies Used: Python, Visual Studio Code, CSV file handling ,Git and GitHub

## Write up
Answer A.  Link to your GitHub repository: 

## Answer B: output of $100,000 USD to CAD

Nuzairaarubaazad@MacBookAir FINE3300-2026-A1 % /usr/bin/python3 /Users/nuzairaarubaazad/Documents/FINE3300-202
6-A1/Exchangerates.py
Enter the amount to convert: 100000
Enter the currency to convert from (USD or CAD): USD
Enter the currency to convert to (USD or CAD): CAD
$139780.00 CAD

nuzairaarubaazad@MacBookAir FINE3300-2026-A1 % /usr/bin/python3 /Users/nuzairaarubaazad/Documents/FINE3300-202
6-A1/Exchangerates.py
Enter the amount to convert: 100000
Enter the currency to convert from (USD or CAD): CAD
Enter the currency to convert to (USD or CAD): USD
$71540.99 USD

## Answer C: LLM Model (GPT - 6)
AI PROMPT: Using the Bank of Canada exchange rate CSV file provided, write a Python program for Part 1 of my FINE 3300 assignment. Do not use any code from me. Create a class called ExchangeRates that reads the CSV file and uses the latest USD/CAD exchange rate to convert between USD and CAD. Include a convert method that accepts an amount, a from-currency, and a to-currency. Prompt the user for these three inputs using input(). Format the output with currency identifiers, dollar signs, commas and 2 decimal places. Use appropriate comments and Python code suitable for a beginner running it in Visual Studio Code. Save the file as ExchangeRatesAI.py. 

## Answer D: comparison of my code vs LLM code.
I used GPT-6 to generate the code for Part 2 of the assignment. Both my original code and the AI-generated code use an `ExchangeRates` class to read the Bank of Canada CSV file and convert amounts between USD and CAD. Despite both giving correct answers, I found my one to be much more simpler to understand. 

Main difference in creating the exchange rates class: However, there are differences in how the two programs read and store the exchange rate. My code uses a `for` loop to iterate through each row in the CSV file and updates the `latest_rate` variable until it contains the last exchange rate. In contrast, the AI-generated code converts the CSV rows into a list and accesses the last row directly using `rows[-1]`. My code stores the exchange rate in an instance attribute called `self.exchange_rate`, whereas the AI-generated code uses `self.usd_cad_rate`. Both programs use conditional statements to determine whether to multiply or divide by the exchange rate. However, my code displays the converted amount with two decimal places, while the AI-generated code also includes commas to make large amounts easier to read. Overall, both approaches achieve the same main objective, but they differ in how they retrieve the latest exchange rate and format the output.
