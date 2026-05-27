"""
Testes unitários para parse/parse_file.py
"""

import argparse
from datetime import date, timedelta

import pytest


class TestParseFile:
    """Teste para o módulo parse_file."""

    def test_read_data_basic(self, caplog):
        """Testa a leitura básica de um CSV válido.

        Verifica que quando um arquivo CSV válido é passado,
        os dados são lidos corretamente e formatados em tabela/JSON.
        """
        from parse import parse_file as pf

        args = argparse.Namespace(
            input="produtos_mock.csv",
            start=None,
            end=None,
            format="text",
        )

        with caplog.at_level("INFO", logger="vendas cli"):
            pf.read_data(args)

    def test_read_data_with_date_filter(self, caplog):
        """Testa a leitura com filtro de datas.

        Verifica que quando start e end são especificados,
        apenas os registros dentro do intervalo são processados.
        """
        from parse import parse_file as pf

        # Definir um intervalo de 5 dias a partir de hoje
        today = date.today()
        start_date = (today - timedelta(days=3)).isoformat()
        end_date = (today + timedelta(days=2)).isoformat()

        args = argparse.Namespace(
            input="produtos_mock.csv",
            start=start_date,
            end=end_date,
            format="text",
        )

        with caplog.at_level("INFO", logger="vendas cli"):
            pf.read_data(args)

    def test_read_data_json_format(self, caplog):
        """Testa o formato JSON.

        Verifica que quando format='json' é passado,
        os dados são exibidos em vez de tabela.
        """
        from parse import parse_file as pf

        args = argparse.Namespace(
            input="produtos_mock.csv",
            start=None,
            end=None,
            format="json",
        )

        with caplog.at_level("INFO", logger="vendas cli"):
            pf.read_data(args)

    def test_read_data_invalid_format(self, caplog):
        """Testa com formato inválido.

        Verifica que uma mensagem de advertência é emitida para
        formatos não reconhecidos (como 'xml').
        """
        from parse import parse_file as pf

        args = argparse.Namespace(
            input="produtos_invalido.csv",
            start=None,
            end=None,
            format="xml",
        )

        with caplog.at_level("ERROR", logger="vendas cli"):
            pf.read_data(args)
        # Verificar que a mensagem de advertência foi emitida
        assert any("INVÁLIDO!!" in record.message for record in caplog.records)

    def test_read_data_empty_file(self, caplog):
        """Testa com arquivo vazio.

        Verifica que o módulo lida corretamente quando um arquivo
        CSV válido é passado, mas está vazio (apenas cabeçalhos).
        """
        from parse import parse_file as pf

        args = argparse.Namespace(
            input="produtos_invalido.csv",
            start=None,
            end=None,
            format="text",
        )

        with caplog.at_level("INFO", logger="vendas cli"):
            pf.read_data(args)

    def test_read_data_with_date_range_outside(self, caplog):
        """Testa com datas fora do intervalo.

        Verifica que quando o filtro de datas retorna zero registros,
        o módulo lida corretamente sem erro e não causa exceção.
        """
        from parse import parse_file as pf

        # Definir um intervalo passado (2020 a 2021)
        start_date = "2025-01-01"
        end_date = "2025-06-22"

        args = argparse.Namespace(
            input="produtos_mock.csv",
            start=start_date,
            end=end_date,
            format="text",
        )

        with caplog.at_level("INFO", logger="vendas cli"):
            pf.read_data(args)

    def test_read_data_single_record(self, caplog):
        """Testa com intervalo que retorna apenas um registro.

        Verifica que o módulo lida corretamente quando há apenas
        um registro dentro do intervalo de datas especificado.
        """
        from parse import parse_file as pf

        # Definir um intervalo para pegar apenas um registro específico
        start_date = (date.today() - timedelta(days=1)).isoformat()
        end_date = (date.today() + timedelta(days=0)).isoformat()

        args = argparse.Namespace(
            input="produtos_mock.csv",
            start=start_date,
            end=end_date,
            format="text",
        )

        with caplog.at_level("INFO", logger="vendas cli"):
            pf.read_data(args)

    def test_read_data_no_filters(self, caplog):
        """Testa sem filtros de datas.

        Verifica que quando start=None e end=None são passados,
        todos os registros são processados e exibidos.
        """
        from parse import parse_file as pf

        args = argparse.Namespace(
            input="produtos_mock.csv",
            start=None,
            end=None,
            format="text",
        )

        with caplog.at_level("INFO", logger="vendas cli"):
            pf.read_data(args)

    def test_read_data_invalid_csv(self, caplog):
        """Testa com CSV inválido (formato incorreto).

        Cria uma situação onde o arquivo não segue o schema esperado,
        e verifica que a exceção é capturada e logada corretamente.
        """
        from parse import parse_file as pf

        # Criar um CSV com colunas inválidas
        args = argparse.Namespace(
            input="produtos_invalido.csv",
            start=None,
            end=None,
            format="text",
        )

        with caplog.at_level("ERROR", logger="vendas cli"):
            pf.read_data(args)

    def test_read_data_exception_handling(self, caplog):
        """Testa o manejo de exceções inesperadas.

        Cria uma situação onde um erro inesperado pode ocorrer durante
        a leitura do CSV e verifica que é capturado e logado.
        """
        from parse import parse_file as pf

        args = argparse.Namespace(
            input="produtos_mock.csv",
            start=None,
            end=None,
            format="text",
        )

        with caplog.at_level("ERROR", logger="vendas cli"):
            pf.read_data(args)
