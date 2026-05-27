import logging
from typing import List, Any, Tuple

from tabulate import tabulate

logger = logging.getLogger(__name__)


def print_table(series: List[Tuple[Any]]) -> None:
    rows: list = []

    # formatar a saida final para tabela
    for r in series:
        rows.append(
            [
                r["id"],
                r["date"],
                r["product"],
                r["quantity"],
                r["current_price"],
                r["total_sales"],
            ]
        )

    logger.info(
        tabulate(
            rows,
            headers=["Id", "Data", "Produto", "Quantidade", "Preço", "Total Vendas"],
            tablefmt="simple_grid",
        )
    )
    logger.info("Total de registros: {}".format(len(rows)))
