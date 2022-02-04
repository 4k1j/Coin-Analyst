import yaml
from pathlib import Path
import os

# env = os.environ["ENVIRONMENT"]
with Path(f"{os.path.realpath(__file__)[:-10]}/config.yaml").open() as config_file:
    CONFIG = yaml.load(config_file, Loader=yaml.FullLoader)