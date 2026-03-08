import requests

def get_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    response = requests.get(url).json()
    if 'price' in response:
        return float(response['price'])
    return None
