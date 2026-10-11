import requests

URL = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 2,
    "sparkline": "false"
}


def get_crypto_data():
    response = requests.get(URL, params=params, timeout=15)

    if response.status_code == 200:
        coins = response.json()

        print("\n===== CRYPTO MARKET TRACKER =====\n")

        for coin in coins:
            print("Name:", coin["name"])
            print("Symbol:", coin["symbol"].upper())
            print("Current Price: $", coin["current_price"])
            print("24h Change:", coin["price_change_percentage_24h"], "%")
            print("Market Cap: $", coin["market_cap"])
            print("-" * 35)
    else:
        print("Error fetching data:", response.status_code)


get_crypto_data()
