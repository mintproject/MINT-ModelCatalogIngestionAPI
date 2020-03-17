#!/usr/bin/env python3

import logging
from pathlib import Path

import connexion
import yaml
from connexion.spec import Specification
from flask_testing import TestCase
from obasparql import QueryManager

from openapi_server import QUERY_DIRECTORY, CONTEXT_DIRECTORY, QUERIES_TYPES
from openapi_server.cached import CachedSpecification
from openapi_server.encoder import JSONEncoder

query_manager = QueryManager(queries_dir=QUERY_DIRECTORY,
                             context_dir=CONTEXT_DIRECTORY,
                             queries_types=QUERIES_TYPES)

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
    post_password = "Cs0WgIQPWJ"

    def login(self):
        query_string = [('username', self.post_username),
                        ('password', self.post_password)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/user/login',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        return response.json


    def create_app(self):
        Specification.from_file = CachedSpecification.from_file

        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml',
                    arguments={'title': 'Model Catalog'},
                    pythonic_params=False,
                    validate_responses=True)
        return app.app
