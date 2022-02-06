import abc
import json
from json import loads
from typing import List

from kafka import KafkaConsumer


class CandleConsumer(abc.ABC):
    def __init__(self, algorithm_name, broker_host, env="dev"):
        self.env = env
        self.topic = f"coin-bot.coin-analyst.{self.env}.{algorithm_name}.candles"
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=[f"{broker_host}:9092"],
            auto_offset_reset="earliest",  # latest, earliest
            # enable_auto_commit=True,
            # group_id="my-group",
            value_deserializer=lambda x: loads(x.decode("utf-8")),
            # consumer_timeout_ms=1000,
        )

    def consume(self):
        for message in self.consumer:
            print(f"Offset : {message.offset}")

            candles = message.value
            if type(candles) == str:
                candles = json.load(message.value)

            self.ingest_candles(candles)

    @abc.abstractmethod
    def ingest_candles(self, candles: List[dict]):
        raise NotImplementedError
