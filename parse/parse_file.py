import argparse
import logging

import pandas
from babel.numbers import format_currency

from output import table, json

logger = logging.getLogger(__name__)

def read_data(args: argparse.Namespace) -> None:
    schema = {
        "id": str,
        "date": str,
        "product": str,
        "quantity": int,
        "price": str
    }
    chunk_size = 1000
    rows = []
    for data in pandas.read_csv(args.input, dtype=schema, chunksize=chunk_size):
        for _, row in data.iterrows():
            # formatar valor para BRL
            row.price = format_currency(row.price, "BRL")
            # adicionar a linha no array
            rows.append(row.values)
        # exibir resultado em formato tabular
        if args.format == "text":
            table.print_table(rows)
        else:
            json.print_json(rows)