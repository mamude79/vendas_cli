import argparse
import logging

from parse import parse_file

logger = logging.getLogger(__name__)

def report(args: argparse.Namespace) -> None:
    if args.format == "text":
        _report_text_output(args)
    elif args.format == "json":
        _report_json_output(args)
    else:
        logger.warning("### FORMATO INVÁLIDO!!! ###")


def _report_text_output(args: argparse.Namespace) -> None:
    logger.info("Relatório em formato tabela")
    parse_file.read_data(args)


def _report_json_output(args: argparse.Namespace) -> None:
    logger.info("Relatório em formato json")
    logger.info(args.input)