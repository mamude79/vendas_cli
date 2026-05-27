import argparse
import logging
from functools import total_ordering

import pandas
from babel.numbers import format_currency
from pandas import Series


from output import table, json

logger = logging.getLogger(__name__)

SCHEMA: dict = {"id": str, "date": str, "product": str, "quantity": int, "price": str}
CHUNK_SIZE: int = 1000


def read_data(args: argparse.Namespace) -> None:
    rows: list = []
    total_sales: float = 0.0
    for data in pandas.read_csv(args.input, dtype=SCHEMA, chunksize=CHUNK_SIZE):

        for _, row in data.iterrows():
            if args.start and args.end:
                start_date = pandas.to_datetime(args.start)
                end_date = pandas.to_datetime(args.end)
                formatted_date = pandas.to_datetime(
                    row["date"], dayfirst=False, errors="coerce"
                )

                if formatted_date >= start_date and formatted_date <= end_date:
                    row = _add_calculations(row)
                    total_sales += float(row.price) * row.quantity
                    rows.append(row)
            else:
                rows.append(row)

    # exibir resultado no formato selecionado
    if args.format == "text":
        table.print_table(rows)
    else:
        json.print_json(rows)

    # Informa o valor total de todas as vendas
    logger.info("Valor total de todas as vendas: {}".format(format_currency(total_sales, "BRL")))

def _add_calculations(row: Series) -> Series:
    row["current_price"] = format_currency(row.price, "BRL")
    row["total_sales"] = format_currency(float(row.price) * row.quantity, "BRL")
    return row
