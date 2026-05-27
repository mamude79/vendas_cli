import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("vendas cli")
logging.basicConfig(level=logging.INFO)
