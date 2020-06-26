#!/usr/bin/env python3
import json
import logging
from pathlib import Path

import connexion
import yaml
from connexion.spec import Specification
from flask_testing import TestCase
from obasparql import QueryManager
from openapi_server.settings import *

from openapi_server import QUERY_DIRECTORY, CONTEXT_DIRECTORY, QUERIES_TYPES
from openapi_server.cached import CachedSpecification
from openapi_server.encoder import JSONEncoder

query_manager = QueryManager(queries_dir=QUERY_DIRECTORY,
                             context_dir=CONTEXT_DIRECTORY,
                             queries_types=QUERIES_TYPES,
                             endpoint=ENDPOINT,
                             endpoint_username=ENDPOINT_USERNAME,
                             endpoint_password=ENDPOINT_PASSWORD,
                             graph_base=ENDPOINT_GRAPH_BASE,
                             prefix=ENDPOINT_RESOURCE_PREFIX)



import logging.config


class BaseTestCase(TestCase):
    logging_file = Path(__file__).parent.parent / "settings" / "logging.ini"
    try:
        logging.config.fileConfig(logging_file)
    except:
        logging.error("Logging config file does not exist {}".format(logging_file))
        exit(0)
    logger = logging.getLogger(__name__)
    get_username = "mint@isi.edu"
    post_username = "mosorio@isi.edu"
    post_password = "jz2KNTg5XgFacX4"

    def login(self):
        data = {"username": self.post_username, "password": self.post_password}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = self.client.open(
            '/v1.5.0/user/login',
            method='POST',
            headers=headers,
            data=json.dumps(data),
            content_type='application/json'
        )
        return response.json


    def create_app(self):
        Specification.from_file = CachedSpecification.from_file

        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml',
                    arguments={'title': 'Model Catalog'},
                    pythonic_params=False,
                    validate_responses=False)
        return app.app
