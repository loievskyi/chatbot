import datetime

from utils.db_api.schemas.exchange_rate import ExchangeRate
from utils.db_api.schemas.last_update_course import LastUpdateCourse


async def get_exchange_rates(base_currency: str):
    pass


async def select_exchange_rates(base_currency: str):
    try:
        exchange_rates = await ExchangeRate.query.where(
            ExchangeRate.base_currency == base_currency).gino.all()
        return exchange_rates
    except Exception as ex:
        print(f"select_exchange_rates failed. {str(ex)}")


async def update_exchange_rates(base_currency: str, exchange_rates: dict):
    try:
        await ExchangeRate.delete.where(ExchangeRate.base_currency == base_currency).gino.status()

        for currency, course in exchange_rates.items():
            await ExchangeRate(base_currency=base_currency,
                               final_curency=currency, course=course).create()

        last_update = await LastUpdateCourse.query.where(
            LastUpdateCourse.currency == base_currency).gino.first()

        if last_update is not None:
            await last_update.update(last_update=datetime.datetime.utcnow()).apply()
        else:
            await LastUpdateCourse.create(currency=base_currency,
                                          last_update=datetime.datetime.utcnow())

    except Exception as ex:
        print(f"update_exchange_rates failed. {str(ex)}")


async def select_last_update_time(currency: str):
    try:
        last_update = await LastUpdateCourse.query.where(
            LastUpdateCourse.currency == currency).gino.first()
        if last_update is not None:
            return last_update.last_update
    except Exception as ex:
        print("select_last_update_time failed. " + str(ex))
