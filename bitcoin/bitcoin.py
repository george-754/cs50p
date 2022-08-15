# Usage bitcoin.py <number of shares> will output the cost that it will take to buy the number of shares of bitcoin

import json
import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Must contain one command-line argument")

    try:
        shares = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-Line argument must be a number")

    total = shares * float(fetch())
    print(f"${total:,.4f}")



def fetch():

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r = response.json()
        
        return r['bpi']['USD']['rate_float'] 
        #print(json.dumps(response.json(), indent=2))
    except requests.RequestException:
        sys.exit("Could not reach API")


if __name__ == "__main__":
    main()