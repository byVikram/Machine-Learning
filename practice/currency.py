import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key

    def convert_currency(self, base_currency, target_currency, amount):
        # Construct the API URL with the base currency, target currency, and API key
        api_url = f'https://v6.exchangerate-api.com/v6/b057f80b8a3efe3000da5792/latest/USD{base_currency}&symbols={target_currency}&access_key={self.api_key}'

        # Send a GET request to the API
        response = requests.get(api_url)
        data = response.json()

        # Check if the API request was successful
        if response.status_code == 200 and data['success']:
            # Get the exchange rate from the response data
            exchange_rate = data['rates'][target_currency]
            # Calculate the converted amount
            converted_amount = amount * exchange_rate

            return converted_amount

        # If the API request failed, return None
        return None


# Usage example
if __name__ == "__main__":
    api_key = "b057f80b8a3efe3000da5792"  # Replace with your actual API key
    converter = CurrencyConverter(api_key)

    base_currency = "USD"
    target_currency = "EUR"
    amount = 100

    converted_amount = converter.convert_currency(base_currency, target_currency, amount)
    if converted_amount is not None:
        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")
    else:
        print("Currency conversion failed.")
