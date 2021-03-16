import datetime
import requests
from utils.db_api.schemas import quick_commands


def format_output_from_request(exchange_rates: dict):
    output = []
    for name, value in exchange_rates.items():
        output.append(f"{name}: {value:.2f}")
    return "\n".join(output)


def format_output_from_db(exchange_rates):
    output = []
    for exchange_rate in exchange_rates:
        currency = exchange_rate.to_dict().get("final_curency")
        course = exchange_rate.to_dict().get("course")
        output.append(f"{currency}: {course:.2f}")
    return "\n".join(output)


def format_to_request_dict(exchange_rates):
    # format exchange_rate from db to request format
    output = dict()
    for exchange_rate in exchange_rates:
        currency = exchange_rate.to_dict().get("final_curency")
        course = exchange_rate.to_dict().get("course")
        output[str(currency)] = float(course)
    return output


async def get_exchange_rates(currency: str):
    try:
        last_update = await quick_commands.select_last_update_time(currency)
    except Exception as ex:
        print(f"get_exchange_rates failed. {str(ex)}")

    if last_update is None or \
        last_update + datetime.timedelta(minutes=10) < datetime.datetime.utcnow():
        response = requests.get(f"https://api.exchangeratesapi.io/latest?base={currency}")
        await quick_commands.update_exchange_rates(currency, response.json()['rates'])

    courses = await quick_commands.select_exchange_rates(currency)
    return courses
