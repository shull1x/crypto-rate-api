from fastapi import FastAPI
from parser import get_crypto_price

app = FastAPI()

@app.get("/price/{symbol}")
def get_price(symbol: str):
    price = get_crypto_price(symbol.upper())
    if price:
        return {"symbol": symbol.upper(), "price": price}
    return {"error": "Криптовалюта не найдена"}
