import abc
from json import dumps
from typing import List
import pandas as pd
from kafka import KafkaProducer

from coin_analyst.consumer import CandleConsumer


class CandleAnalyst(CandleConsumer):
    def __init__(self, algorithm_name, broker_host, env="dev"):
        super().__init__(algorithm_name, broker_host, env)

        self.topic = f"coin-bot.coin-analyst.{self.env}.{algorithm_name}.result"

        self.producer = KafkaProducer(
            acks=0,
            compression_type="gzip",
            bootstrap_servers=[f"{broker_host}:9092"],
            value_serializer=lambda x: dumps(x).encode("utf-8"),
        )

    @abc.abstractmethod
    def analysis(self, candles: List[dict]) -> dict:
        raise NotImplementedError

    def ingest_candles(self, candles: List[dict]):
        result = self.analysis(candles)
        self.send_result(result)

    def send_result(self, result: dict):
        response = self.producer.send(self.topic, value=result)
        self.producer.flush()


class SimpleAnalyst(CandleAnalyst):
    def analysis(self, candles: List[dict]) -> dict:
        df = pd.DataFrame(candles)

        result = df["open_price"].sum()
        print(result)
        return {"result": result}
