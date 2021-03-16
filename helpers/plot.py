import time
import os
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fill_empty_days(dates: list, rates: list, start_day: str, curent_day: str):
    dates_range = pd.date_range(start=pd.to_datetime(start_day),
                                end=pd.to_datetime(curent_day))
    for date in dates_range:
        if date not in dates:
            dates.append(date)
            rates.append(None)


def has_empty_days(dates: list, start_day: str, curent_day: str):
    dates_range = pd.date_range(start=pd.to_datetime(start_day),
                                end=pd.to_datetime(curent_day))
    for date in dates_range:
        if date not in dates:
            return True

    return False


def create_graph(data: dict, base_curency: str, final_curency: str,
                 start_day: str, curent_day: str, title: str=""):
    plt.close("all")
    dates = list()
    rates = list()
    base_path = Path(__file__).resolve().parent.parent
    file_name = os.path.join(base_path, "images", str(time.time()) + ".png")

    for date, values in data.get("rates").items():
        dates.append(pd.to_datetime(date))
        rates.append(values.get(final_curency))

    # fill_empty_days(dates, rates, start_day, curent_day)
    df = pd.DataFrame({"dates": dates, "rates": rates})
    df = df.sort_values(by="dates")
    if has_empty_days(dates=dates, start_day=start_day, curent_day=curent_day):
        title = "No exchange rate data is available for the selected currency. \n" + title

    plt.plot()
    plot = df.plot(x="dates", y="rates", kind="line", title=title, legend=True,
                   xlabel="dates", ylabel="exchange rates", figsize=(12, 8),
                   grid=True)
    plot.legend([f"{base_curency}/{final_curency}"])
    plt.savefig(file_name)

    return file_name, title
