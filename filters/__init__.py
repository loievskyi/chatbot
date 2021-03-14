from .list_rates import IsListRates
from .exchange import IsExchange, IsExchangeCorrectFormat
from .history import IsHistory, IsHistoryCorrectFormat
from loader import dp


if __name__ == "filters":
    dp.bind_filter(IsListRates)
    dp.bind_filter(IsExchange)
    dp.bind_filter(IsExchangeCorrectFormat)
    dp.bind_filter(IsHistory)
    dp.bind_filter(IsHistoryCorrectFormat)
