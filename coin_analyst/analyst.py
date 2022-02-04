from typing import List
import pandas as pd
from coin_analyst.consumer import CandleConsumer


class SimpleCandleAnalyst(CandleConsumer):
    def exploit_candles(self, candles: List[dict]):
        df = pd.DataFrame(candles)

        result = df["open_price"].sum()


