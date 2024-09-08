import requests
import sys
import sys
import requests

def main():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        price = data['bpi']['USD']['rate']
    except requests.RequestException:
        print("Error: Unable to retrieve Bitcoin price data.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)
    elif len(sys.argv) >= 3:
        print("Too many arguments")
        sys.exit(1)

    try:
        multiplier = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:    print(f"${formatted_price}")

        int_price = float(price.replace(',', ''))
        mult_price = multiplier * int_price
    except ValueError:
        print("Error: Unexpected data format.")
        sys.exit(1)

    formatted_price = "{:,.4f}".format(mult_price)


main()



