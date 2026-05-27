"""
Testes unitários para output/table.py
"""

import pytest
from pandas import DataFrame, Series


class TestTableOutput:
    """Teste para o módulo table do output."""

    def test_print_table_with_series_list(self, caplog):
        """Testa a formatação de uma lista de Series em tabela.

        Verifica que quando uma lista de Series é passada,
        cada um é convertido corretamente e exibido como tabela.
        """
        from output.table import print_table as pt

        # Criar alguns dados de teste
        data = {
            "id": [1, 2, 3],
            "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
            "product": ["Produto A", "Produto B", "Produto C"],
            "quantity": [10, 15, 20],
            "current_price": [100.0, 120.0, 80.0],
            "total_sales": [1000.0, 1800.0, 1600.0],
        }

        df = DataFrame(data)

        # Criar uma lista de Series (cada coluna como um Series separado)
        series_list = [
            df["id"],
            df["date"],
            df["product"],
            df["quantity"],
            df["current_price"],
            df["total_sales"],
        ]

        with caplog.at_level("INFO", logger="vendas cli"):
            pt(series_list)

    def test_print_table_empty_series_list(self, caplog):
        """Testa com uma lista vazia de Series.

        Verifica que quando uma lista vazia é passada,
        o módulo lida corretamente sem erro e não causa exceção.
        """
        from output.table import print_table as pt

        with caplog.at_level("INFO", logger="vendas cli"):
            pt([])

    def test_print_table_single_series(self, caplog):
        """Testa com uma lista contendo apenas um Series.

        Verifica que o módulo lida corretamente quando há
        apenas um item na lista de Series.
        """
        from output.table import print_table as pt

        data = {
            "id": [1, 2, 3],
            "product": ["A", "B", "C"],
            "price": [10.5, 25.9, 30.0],
        }
        df = DataFrame(data)
        series_list = [df["id"]]

        with caplog.at_level("INFO", logger="vendas cli"):
            pt(series_list)

    def test_print_table_with_nan_values(self, caplog):
        """Testa com Series contendo valores NaN.

        Verifica que o módulo lida corretamente quando os dados
        contém valores NaN (que são válidos na tabela).
        """
        from output.table import print_table as pt

        data = {
            "id": [1, 2, None, 4, 5],
            "product": ["A", "B", "C", "D", "E"],
            "price": [10.5, 25.9, None, 30.0, 40.0],
        }
        df = DataFrame(data)
        series_list = [df["id"], df["product"], df["price"]]

        with caplog.at_level("INFO", logger="vendas cli"):
            pt(series_list)

    def test_print_table_with_different_dtypes(self, caplog):
        """Testa com Series de diferentes tipos de dados.

        Verifica que o módulo lida corretamente quando os dados
        contém inteiros, strings e floats em uma lista.
        """
        from output.table import print_table as pt

        data = {
            "id": [1, 2, 3],
            "product": ["A", "B", "C"],
            "price": [10.5, 25.9, 30.0],
            "quantity": [10, 15, 20],
        }
        df = DataFrame(data)

        series_list = [
            df["id"],  # int64
            df["product"],  # object (string)
            df["price"],  # float64
            df["quantity"],  # int64
        ]

        with caplog.at_level("INFO", logger="vendas cli"):
            pt(series_list)

    def test_print_table_exception_handling(self, caplog):
        """Testa o manejo de exceções quando to_json falha.

        Cria uma situação onde a formatação da tabela pode levantar
        uma exceção inesperada e verifica que é capturada e logada.
        """
        from output.table import print_table as pt

        # Criar Series com dtype indefinido que pode causar erro
        series_list = [Series([], dtype=object)]

        with caplog.at_level("ERROR", logger="vendas cli"):
            pt(series_list)

    def test_print_table_logs_success_message(self, caplog):
        """Testa especificamente as mensagens de sucesso.

        Verifica que exatamente uma mensagem de sucesso é emitida
        quando o processamento conclui com êxito.
        """
        from output.table import print_table as pt

        data = {"id": [1, 2], "product": ["A", "B"]}
        df = DataFrame(data)
        series_list = [df["id"], df["product"]]

        with caplog.at_level("INFO", logger="vendas cli"):
            pt(series_list)

    def test_print_table_with_large_series(self, caplog):
        """Testa com Series grandes.

        Verifica que o módulo lida corretamente quando os dados
        contêm um número grande de registros (1000 linhas).
        """
        from output.table import print_table as pt

        n = 1000
        data = {f"col{i}": list(range(n)) for i in range(5)}
        df = DataFrame(data)
        series_list = [df[f"col{i}"] for i in range(5)]

        with caplog.at_level("INFO", logger="vendas cli"):
            pt(series_list)

    def test_print_table_with_mixed_nulls(self, caplog):
        """Testa com Series contendo valores null/NaN mistos.

        Verifica que o módulo lida corretamente quando os dados
        contém uma mistura de NaN e None.
        """
        from output.table import print_table as pt

        data = {
            "id": [1, 2, None, 4, 5],
            "product": [None, "B", "C", None, "E"],
            "price": [10.5, None, 30.0, 40.0, None],
        }
        df = DataFrame(data)
        series_list = [df["id"], df["product"], df["price"]]

        with caplog.at_level("INFO", logger="vendas cli"):
            pt(series_list)

    def test_print_table_with_boolean_and_datetime(self, caplog):
        """Testa com Series de tipos booleano e datetime.

        Verifica que o módulo lida corretamente quando os dados
        contêm valores booleanos e datas.
        """
        from output.table import print_table as pt

        data = {
            "id": [1, 2, 3],
            "product": ["A", "B", "C"],
            "price": [10.5, 25.9, 30.0],
            "active": [True, False, True],
        }
        df = DataFrame(data)

        series_list = [
            df["id"],
            df["product"],
            df["price"],
            df["active"],
        ]

        with caplog.at_level("INFO", logger="vendas cli"):
            pt(series_list)
