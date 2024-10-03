import requests # type: ignore

def get_crypto_price(crypto='bitcoin', currency='usd'):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': crypto,
        'vs_currencies': currency
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data[crypto][currency]

print(f"Bitcoin Price: ${get_crypto_price()}")
