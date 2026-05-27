import argparse
import locale

from core.report_generator import report
from log import logger


def main():
    parse = argparse.ArgumentParser(prog="vendas_cli")
    parse.add_argument("--input", "-i", required=True)
    parse.add_argument("--format", "-f", required=True)
    parse.add_argument("--start", "-s")
    parse.add_argument("--end", "-e")
    args = parse.parse_args()

    logger.info("Gerando relatório de vendas")

    # montar relatório
    report(args)

    logger.info("Fim do relatório...")


if __name__ == "__main__":
    main()
