import time
import os
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fill_empty_days(dates: list, rates: list):
    dates_range = pd.date_range(start=min(dates), end=max(dates))
    for date in dates_range:
        if date not in dates:
            dates.append(date)
            rates.append(None)


def create_graph(data: dict, base_curency: str, final_curency: str, title: str=""):
    plt.close("all")
    dates = list()
    rates = list()
    base_path = Path(__file__).resolve().parent.parent
    file_name = os.path.join(base_path, "images", str(time.time()) + ".png")

    for date, values in data.get("rates").items():
        dates.append(pd.to_datetime(date))
        rates.append(values.get(final_curency))

    # fill_empty_days(dates, rates)
    df = pd.DataFrame({"dates": dates, "rates": rates})
    df = df.sort_values(by="dates")

    plt.plot()
    plot = df.plot(x="dates", y="rates", kind="line", title=title, legend=True,
                   xlabel="dates", ylabel="exchange rates", figsize=(12, 8),
                   grid=True)
    plot.legend([f"{base_curency}/{final_curency}"])
    plt.savefig(file_name)

    return file_name
