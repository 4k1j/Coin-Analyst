from coin_analyst.analyst import SimpleAnalyst
from config.config import CONFIG

if __name__ == '__main__':
    kafka_config = CONFIG["kafka"]
    analyst = SimpleAnalyst("test", kafka_config["broker"]["host"])
    analyst.consume()


