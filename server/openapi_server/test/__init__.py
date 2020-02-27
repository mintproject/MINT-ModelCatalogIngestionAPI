#!/usr/bin/env python3

import logging

import connexion
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
import os

# Disable Django's logging setup
LOGGING_CONFIG = None

LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        # console logs to stderr
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        # default for all undefined Python modules
        '': {
            'level': 'WARNING',
            'handlers': ['console'],
        },
        # Our application code
        'openapi_server': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            # Avoid double logging because of root logger
            'propagate': False,
        },
        # Prevent noisy modules from logging to Sentry
        'noisy_module': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
})
logger = logging.getLogger(__name__)


class BaseTestCase(TestCase):
    def setup(self):
        self.get_username = "mint@isi.edu"

    def create_app(self):
        logger = logging.getLogger(__name__)
        logging.getLogger('connexion.operation').setLevel('ERROR')
        logging.getLogger('connexion').setLevel('ERROR')

        Specification.from_file = CachedSpecification.from_file

        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml',
                    arguments={'title': 'Model Catalog'},
                    pythonic_params=False)
        return app.app
