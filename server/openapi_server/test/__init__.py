import logging
from pathlib import Path
import connexion
from flask_testing import TestCase
from openapi_server.cached import CachedSpecification
from openapi_server.encoder import JSONEncoder
from openapi_server.settings import *
from connexion.spec import Specification

import logging.config
from obasparql import QueryManager


query_manager = QueryManager(queries_dir=QUERY_DIRECTORY,
                            context_dir=CONTEXT_DIRECTORY,
                            queries_types=QUERIES_TYPES,
                            endpoint=ENDPOINT,
                            endpoint_username=ENDPOINT_USERNAME,
                            endpoint_password=ENDPOINT_PASSWORD,
                            graph_base=ENDPOINT_GRAPH_BASE,
                            prefix=ENDPOINT_RESOURCE_PREFIX)



class BaseTestCase(TestCase):
    logging_file = Path(__file__).parent.parent / "settings" / "logging.ini"
    try:
        logging.config.fileConfig(logging_file)
    except:
        logging.error("Logging config file does not exist {}".format(logging_file))
        exit(0)
    logger = logging.getLogger(__name__)

    def create_app(self):
        Specification.from_file = CachedSpecification.from_file
        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml',
                    pythonic_params=False,
                    validate_responses=True)
        return app.app
