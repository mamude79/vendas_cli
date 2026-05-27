import logging
from typing import List, Any

from tabulate import tabulate

logger = logging.getLogger(__name__)

def print_table(rows: List[Any]) -> None:
    logger.info(tabulate(rows, headers=["Id", "Date", "Product", "Quantity", "Price"], tablefmt="simple_grid"))