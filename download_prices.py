import os
from typing import List

import yfinance as yf

from utils import get_sp500_tickers


def export_prices(tickers: List[str], storage_path: str):
    data = yf.download(
        ' '.join(tickers),
        start="2016-01-01",
        end="2021-01-01",
        threads=True,
        interval='1d'
    )
    data = data.stack()
    data = data.loc[:, ['Close']]
    data = data.unstack()

    data.to_csv(os.path.join(storage_path, 'prices.csv'))


if __name__ == '__main__':
    tickers = get_sp500_tickers()
    export_prices(tickers, './data')