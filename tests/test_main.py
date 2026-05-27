import argparse
from unittest.mock import patch, MagicMock
import pytest
from main import main


class TestMain:
    """Testes unitários para o módulo main.py do vendas-cli."""

    @patch("main.report")
    def test_main_executes_with_valid_arguments(self, mock_report):
        """Testa que main executa corretamente com argumentos válidos."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start=None, end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            # Verifica que report foi chamado com os argumentos corretos
            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_format_table(self, mock_report):
        """Testa que main executa quando format="table"."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start=None, end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_format_json(self, mock_report):
        """Testa que main executa quando format="json"."""
        args = argparse.Namespace(
            input="produtos.csv", format="json", start=None, end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_date_range(self, mock_report):
        """Testa que main executa com intervalo de datas especificado."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start="2024-01-01", end="2024-12-31"
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            # Verifica que report foi chamado com o intervalo de datas
            call_args = mock_report.call_args[0][0]
            assert call_args.start == "2024-01-01"
            assert call_args.end == "2024-12-31"

    @patch("main.report")
    def test_main_executes_with_only_start_date(self, mock_report):
        """Testa que main executa com apenas data inicial especificada."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start="2024-01-01", end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_only_end_date(self, mock_report):
        """Testa que main executa com apenas data final especificada."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start=None, end="2024-12-31"
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_without_date_range(self, mock_report):
        """Testa que main executa sem intervalo de datas especificado."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start=None, end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_all_options(self, mock_report):
        """Testa que main executa com todas as opções possíveis."""
        args = argparse.Namespace(
            input="produtos.csv", format="json", start="2024-01-01", end="2024-12-31"
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            call_args = mock_report.call_args[0][0]
            assert call_args.input == "produtos.csv"
            assert call_args.format == "json"
            assert call_args.start == "2024-01-01"
            assert call_args.end == "2024-12-31"

    @patch("main.report")
    def test_main_executes_with_short_flag_format_table(self, mock_report):
        """Testa que main executa usando o flag curto -f."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start=None, end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_short_flag_format_json(self, mock_report):
        """Testa que main executa usando o flag curto -f."""
        args = argparse.Namespace(
            input="produtos.csv", format="json", start=None, end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_short_flag_input(self, mock_report):
        """Testa que main executa usando o flag curto -i."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start=None, end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_short_flag_start(self, mock_report):
        """Testa que main executa usando o flag curto -s."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start="2024-01-01", end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_short_flag_end(self, mock_report):
        """Testa que main executa usando o flag curto -e."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start=None, end="2024-12-31"
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_without_date_range_short_flags(self, mock_report):
        """Testa que main executa sem intervalo de datas usando flags curtos."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start=None, end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_date_range_short_flags(self, mock_report):
        """Testa que main executa com intervalo de datas usando flags curtos."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start="2024-01-01", end="2024-12-31"
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            call_args = mock_report.call_args[0][0]
            assert call_args.start == "2024-01-01"
            assert call_args.end == "2024-12-31"

    @patch("main.report")
    def test_main_executes_with_only_start_date_short_flag(self, mock_report):
        """Testa que main executa com apenas data inicial usando flag curto."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start="2024-01-01", end=None
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)

    @patch("main.report")
    def test_main_executes_with_only_end_date_short_flag(self, mock_report):
        """Testa que main executa com apenas data final usando flag curto."""
        args = argparse.Namespace(
            input="produtos.csv", format="table", start=None, end="2024-12-31"
        )

        with patch.object(argparse, "ArgumentParser") as mock_parser:
            mock_parser_instance = MagicMock()
            mock_parser_instance.parse_args.return_value = args
            mock_parser.return_value = mock_parser_instance

            main()

            mock_report.assert_called_once_with(args)
