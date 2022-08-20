import asyncio
import json
import os
import re

import requests
from binance import AsyncClient, BinanceSocketManager
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env file
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")
token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")


def fix_float(float_num):
    regex = r"(\.\d+?)0+\b"
    subst = "\\1"
    result = re.sub(regex, subst, str(float_num), 0)
    return result


def send_telegram(text):
    try:
        dt = {'chat_id': chat_id, 'text': text, 'parse_mode': "html"}
        res = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage", params=dt)
        ok = res.json()
        if not ok['ok']:
            print(f"Error From telegram: {ok}")
    except Exception as E:
        print(
            f"Exception on processing send_telegram https requests: {str(E)}")


def base(symbol_: str) -> str:
    str3 = symbol_[-3:]
    str4 = symbol_[-4:]
    if str4 in ["USDT", "BUSD", "TUSD", "USDC", "BIDR", "IDRT", "BVND"]:
        return str4
    elif str3 in ["BNB", "BTC", "XRP", "TRX", "ETH", "AUD", "BRL", "EUR", "GBP", "RUB", "TRY", "PAX", "DAI", "UAH",
                  "NGN", "VAI"]:
        return str3
    else:
        return str("Unknown")


def target(symbol_: str, length: int):
    c = symbol_[:-length]
    return c


def process_message(json_data):
    try:
        event_type = json_data['e']
        if event_type == 'executionReport':
            symbol = json_data['s']
            price = fix_float(json_data['p'])
            quantity = fix_float(json_data['q'])
            side = json_data['S']
            order_id = json_data['i']
            order_status = json_data['X']
            last_trade_quantity = fix_float(json_data['l'])
            filled_qty = fix_float(json_data['z'])
            order_type = json_data['o']
            last_price = fix_float(json_data['L'])
            bc = base(symbol)
            tc = target(symbol, len(bc))

            if order_type == "MARKET":
                final_price = last_price
            else:
                final_price = price

            if order_status == 'NEW':
                txt = (f"✅ <b>Spot {side} {order_type} Order CREATED\n"
                       f"Symbol:  {symbol}\n"
                       f"Price:  {final_price} {bc}\n"
                       f"Quantity:  {quantity} {tc}\n"
                       f"OrderID:  {order_id}</b>")

            elif order_status == 'CANCELED':
                txt = (f"❎ <b>Spot {side} {order_type} Order CANCELED\n"
                       f"Symbol:  {symbol}\n"
                       f"Price:  {final_price} {bc}\n"
                       f"Quantity:  {quantity} {tc}\n"
                       f"OrderID:  {order_id}</b>")

            elif order_status == 'PARTIALLY_FILLED':
                txt = (f"⌛️ <b>Spot {side} {order_type} Order PARTIALLY FILLED\n"
                       f"Symbol:  {symbol}\n"
                       f"Price:  {last_price} {bc}\n"
                       f"Last Filled:  {last_trade_quantity} {tc}\n"
                       f"Total Filled:  {filled_qty} {tc}\n"
                       f"Remaining:  {float(quantity) - float(filled_qty)} {tc}\n"
                       f"OrderID:  {order_id}</b>")

            elif order_status == 'FILLED':
                txt = (f"💰 <b>Spot {side} {order_type} Order FULLY FILLED\n"
                       f"Symbol:  {symbol}\n"
                       f"Average Price:  {fix_float(float(json_data['Z']) / float(json_data['z']))} {bc}\n"
                       f"Filled:  {filled_qty} {tc}\n"
                       f"OrderID:  {order_id}</b>")
            else:
                txt = f"<b>Spot {side} {order_type} Order {order_status}\n" \
                      f"Symbol:  {symbol}\nPrice:  {final_price} {bc}\n" \
                      f"Quantity:  {quantity} {tc}\n" \
                      f"OrderID:  {order_id}</b>"
            send_telegram(txt)

    except Exception as E:
        ee = str(f"In spot, Exception found on processed message: {str(E)}")
        print(ee)
        send_telegram(ee)


async def spot_user(client):
    bm = BinanceSocketManager(client, user_timeout=1700)
    t = f"Binance Starts a web socket Manager for spot.."
    print(t)
    send_telegram(t)
    async with bm.user_socket() as stream:
        while True:
            res = await stream.recv()
            if res is not None and "e" in res:
                process_message(res)
                print(json.dumps(res, indent=2))
            else:
                print(res)


async def main():
    client = await AsyncClient.create(api_key=api_key, api_secret=api_secret)
    await spot_user(client=client)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
