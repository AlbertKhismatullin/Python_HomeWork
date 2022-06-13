import requests
from dateutil.parser import parse 

def get_all_exchange_rates_erapi(src):
    url = f"https://open.er-api.com/v6/latest/{src}"
    data = requests.get(url).json()
    if data["result"] == "success":
        last_updated_datetime = parse(data["time_last_update_utc"])
        exchange_rates = data["rates"]
    return last_updated_datetime, exchange_rates
        
        

def convert_currency_erapi(src, dst, amount):
    last_updated_datetime, exchange_rates = get_all_exchange_rates_erapi(src)
    return last_updated_datetime, exchange_rates[dst] * amount


if __name__ == "__main__":
    import sys
    source_currency = sys.argv[1]
    destination_currency = sys.argv[2]
    amount = float(sys.argv[3])
    last_updated_datetime, exchange_rate = convert_currency_erapi(source_currency, destination_currency, amount)
    print("Last updated datetime:", last_updated_datetime)
    print(f"{amount} {source_currency} = {exchange_rate} {destination_currency}")
    
    # для конвертации валют введите :
    # python currency_converter_erapi.py EUR RUB 1000 (вместо EUR, RUB, 1000 можно вводить любые другие значения)
