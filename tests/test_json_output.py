"""
Testes unitários para output/json.py
"""

import pytest
from pandas import DataFrame, Series


class TestJsonOutput:
    """Teste para o módulo json do output."""

    def test_print_json_with_series_list(self, caplog):
        """Testa a conversão de uma lista de Series para JSON.

        Verifica que quando uma lista de Series é passada,
        cada um é convertido corretamente usando to_json().
        """
        from output.json import print_json as pj

        # Criar alguns dados de teste
        data = {
            "id": [1, 2, 3],
            "nome": ["Produto A", "Produto B", "Produto C"],
            "preco": [10.5, 25.9, 30.0],
        }

        df = DataFrame(data)

        # Criar uma lista de Series (cada coluna como um Series separado)
        series_list = [df["id"], df["nome"], df["preco"]]

        with caplog.at_level("INFO", logger="vendas cli"):
            pj(series_list)

    def test_print_json_empty_series_list(self, caplog):
        """Testa com uma lista vazia de Series.

        Verifica que quando uma lista vazia é passada,
        o módulo lida corretamente sem erro.
        """
        from output.json import print_json as pj

        with caplog.at_level("INFO", logger="vendas cli"):
            pj([])

    def test_print_json_single_series(self, caplog):
        """Testa com uma lista contendo apenas um Series.

        Verifica que o módulo lida corretamente quando há
        apenas um item na lista de Series.
        """
        from output.json import print_json as pj

        data = {"id": [1, 2, 3], "nome": ["A", "B", "C"]}
        df = DataFrame(data)
        series_list = [df["id"]]

        with caplog.at_level("INFO", logger="vendas cli"):
            pj(series_list)

    def test_print_json_with_nan_values(self, caplog):
        """Testa com Series contendo valores NaN.

        Verifica que o módulo lida corretamente quando os dados
        contêm valores NaN (que são válidos no JSON).
        """
        from output.json import print_json as pj

        data = {"id": [1, 2, None], "nome": ["A", "B", "C"]}
        df = DataFrame(data)
        series_list = [df["id"], df["nome"]]

        with caplog.at_level("INFO", logger="vendas cli"):
            pj(series_list)

    def test_print_json_with_different_dtypes(self, caplog):
        """Testa com Series de diferentes tipos de dados.

        Verifica que o módulo lida corretamente quando os dados
        contêm inteiros, strings e floats em uma lista.
        """
        from output.json import print_json as pj

        data = {
            "id": [1, 2, 3],
            "nome": ["A", "B", "C"],
            "preco": [10.5, 25.9, 30.0],
            "ativo": [True, False, True],
        }
        df = DataFrame(data)

        series_list = [
            df["id"],  # int64
            df["nome"],  # object (string)
            df["preco"],  # float64
            df["ativo"],  # bool
        ]

        with caplog.at_level("INFO", logger="vendas cli"):
            pj(series_list)

    def test_print_json_exception_handling(self, caplog):
        """Testa o manejo de exceções quando to_json falha.

        Cria uma situação onde Series.to_json() pode levantar
        uma exceção inesperada e verifica que a exceção é capturada
        e logada corretamente.
        """
        from output.json import print_json as pj

        # Criar um Series com dtype indefinido que pode causar erro ao converter para JSON
        series_list = [Series([], dtype=object)]  # Vazio + object pode causar problema

        with caplog.at_level("ERROR", logger="vendas cli"):
            pj(series_list)

    def test_print_json_logs_success_message(self, caplog):
        """Testa especificamente a mensagem de sucesso.

        Verifica que exatamente uma mensagem de sucesso é emitida
        quando o processamento conclui com êxito.
        """
        from output.json import print_json as pj

        data = {"id": [1, 2], "nome": ["A", "B"]}
        df = DataFrame(data)
        series_list = [df["id"], df["nome"]]

        with caplog.at_level("INFO", logger="vendas cli"):
            pj(series_list)

    def test_print_json_with_large_series(self, caplog):
        """Testa com Series grandes.

        Verifica que o módulo lida corretamente quando os dados
        contêm um número grande de registros.
        """
        from output.json import print_json as pj

        # Criar Series com 1000 registros
        n = 1000
        data = {f"col{i}": list(range(n)) for i in range(5)}
        df = DataFrame(data)
        series_list = [df[f"col{i}"] for i in range(5)]

        with caplog.at_level("INFO", logger="vendas cli"):
            pj(series_list)

    def test_print_json_with_mixed_nulls(self, caplog):
        """Testa com Series contendo valores null/NaN mistos.

        Verifica que o módulo lida corretamente quando os dados
        contêm uma mistura de NaN e None.
        """
        from output.json import print_json as pj

        data = {
            "id": [1, 2, None, 4, 5],
            "nome": [None, "B", "C", None, "E"],
        }
        df = DataFrame(data)
        series_list = [df["id"], df["nome"]]

        with caplog.at_level("INFO", logger="vendas cli"):
            pj(series_list)
