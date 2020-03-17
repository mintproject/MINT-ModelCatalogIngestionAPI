import logging.config
from pathlib import Path

from obasparql import QueryManager
from openapi_server.settings import CONTEXT_DIRECTORY, QUERY_DIRECTORY, QUERIES_TYPES, logging_file

try:
    logging.config.fileConfig(logging_file)
except:
    logging.error("Logging config file does not exist {}".format(logging_file))
    exit(0)

logger = logging.getLogger(__name__)
query_manager = QueryManager(queries_dir=QUERY_DIRECTORY,
                             context_dir=CONTEXT_DIRECTORY,
                             queries_types=QUERIES_TYPES)




