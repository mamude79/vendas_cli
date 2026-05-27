import json

from typing import List

from pandas import Series

from log import logger

def print_json(series: List[Series]) -> None:
    converted = [s.to_json() for s in series]
    logger.info(json.dumps(converted, indent=2))
