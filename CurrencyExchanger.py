import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("CE_API_KEY")

while True:
    base_currency = input("Please enter your base currency with the internationally accepted 3 letter abbreviation (or exit): ")
    if base_currency.lower() == "exit":
        break
    else:  
        target_currency = input("Please enter your target currency with the internationally accepted 3 letter abbreviation: ")
        amount = float(input("How much would you like to convert? "))

        try:
            b = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency.upper()}")
            rate = b.json()["conversion_rates"][target_currency.upper()]
            print(f"{amount} {base_currency.upper()} = {amount * rate} {target_currency.upper()}")
        except:
            print("There seems to be an issue with accessing the API... please try again.")
            continue