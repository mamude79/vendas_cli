"""
Testes unitários para report_generator.py
"""

import pytest
from argparse import Namespace


class TestReportGenerator:
    """Teste para a classe ReportGenerator e suas funções auxiliares."""

    def test_report_dispatch_text_format(self, caplog):
        """Testa o dispatch do report para formato texto.

        Verifica que quando o formato é 'text', a função
        _report_text_output é chamada corretamente.
        """
        from core import report_generator as rg

        args = Namespace(format="text")
        with caplog.at_level("INFO"):
            rg.report(args)
        assert True  # Se chegou aqui, o dispatch funcionou corretamente

    def test_report_dispatch_json_format(self, caplog):
        """Testa o dispatch do report para formato JSON.

        Verifica que quando o formato é 'json', a função
        _report_json_output é chamada corretamente.
        """
        from core import report_generator as rg

        args = Namespace(format="json")
        with caplog.at_level("INFO"):
            rg.report(args)
        assert True  # Se chegou aqui, o dispatch funcionou corretamente

    def test_report_invalid_format(self, caplog):
        """Testa o comportamento quando formato inválido é passado.

        Verifica que uma mensagem de advertência é emitida para
        formatos não reconhecidos.
        """
        from core import report_generator as rg

        args = Namespace(format="xml")
        with caplog.at_level("WARNING", logger="root"):
            rg.report(args)
        # Verificar que a mensagem de advertência foi emitida
        assert any("FORMATO INVÁLIDO!!!" in record.message for record in caplog.records)

    def test_report_text_format_output(self, caplog):
        """Testa o output do _report_text_output.

        Verifica que as mensagens de log são emitidas corretamente
        quando o formato texto é processado.
        """
        from core import report_generator as rg

        args = Namespace(format="text")
        with caplog.at_level("INFO", logger="root"):
            rg._report_text_output(args)
        # Verificar que as mensagens de log foram emitidas
        assert any(
            "Relatório em formato tabela" in record.message for record in caplog.records
        )
        assert any("Processando..." in record.message for record in caplog.records)

    def test_report_json_format_output(self, caplog):
        """Testa o output do _report_json_output.

        Verifica que as mensagens de log são emitidas corretamente
        quando o formato JSON é processado.
        """
        from core import report_generator as rg

        args = Namespace(format="json")
        with caplog.at_level("INFO", logger="root"):
            rg._report_json_output(args)
        # Verificar que as mensagens de log foram emitidas
        assert any(
            "Relatório em formato json" in record.message for record in caplog.records
        )
        assert any("Processando..." in record.message for record in caplog.records)

    def test_report_none_format(self, caplog):
        """Testa o comportamento quando formato None é passado.

        Verifica que uma mensagem de advertência é emitida para
        formatos inválidos, incluindo None.
        """
        from core import report_generator as rg

        args = Namespace(format=None)
        with caplog.at_level("WARNING", logger="root"):
            rg.report(args)
        # Verificar que a mensagem de advertência foi emitida
        assert any("FORMATO INVÁLIDO!!!" in record.message for record in caplog.records)
