import argparse
from collections import defaultdict

import pandas
from babel.numbers import format_currency
from pandas import Series

from output import json, table

from log import logger

SCHEMA: dict = {"id": str, "date": str, "product": str, "quantity": int, "price": str}
CHUNK_SIZE: int = 1000


def read_data(args: argparse.Namespace) -> None:
    try:
        rows: list = []
        total_sales: float = 0.0
        product_totals = defaultdict(int)

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
                        total_sales += _sum_total_sales(row)
                        _get_product_groupby_sales(row, product_totals)
                        rows.append(row)
                else:
                    row = _add_calculations(row)
                    total_sales += _sum_total_sales(row)
                    _get_product_groupby_sales(row, product_totals)
                    rows.append(row)

        # exibir resultado no formato selecionado
        if args.format == "text":
            table.print_table(rows)
        else:
            json.print_json(rows)

        # Informa o valor total de todas as vendas
        logger.info(
            "Valor total de todas as vendas: {}".format(
                format_currency(total_sales, "BRL")
            )
        )
        # Ordena e pegar o produto mais vendido
        sorted_products = sorted(
            product_totals.items(), key=lambda x: x[1], reverse=True
        )
        best_product = sorted_products[0][0] if sorted_products else ""
        max_quantity = sorted_products[0][1] if sorted_products else 0

        logger.info("Produto mais vendido: {} - {}".format(best_product, max_quantity))
    except AttributeError, Exception:
        logger.error("### FORMATO DO CSV INVÁLIDO!!! ###")


def _add_calculations(row: Series) -> Series:
    row["current_price"] = format_currency(
        row.price, currency="BRL", locale="pt_BR", format="R$ #,##0.##"
    )
    row["total_sales"] = format_currency(
        float(row.price) * row.quantity,
        currency="BRL",
        locale="pt_BR",
        format="R$ #,##0.##",
    )
    return row


def _sum_total_sales(row: Series) -> float:
    return float(row.price) * row.quantity


def _get_product_groupby_sales(row: Series, product_totals: dict) -> None:
    if row["quantity"] > 0 and pandas.notna(row["quantity"]):
        product = row["product"]
        current_total = product_totals.get(product, 0)
        product_totals[product] = current_total + int(row["quantity"])
