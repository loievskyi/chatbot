from .exchange import IsExchange, IsExchangeCorrectFormat
from loader import dp


if __name__ == "filters":
    dp.bind_filter(IsExchange)
    dp.bind_filter(IsExchangeCorrectFormat)
