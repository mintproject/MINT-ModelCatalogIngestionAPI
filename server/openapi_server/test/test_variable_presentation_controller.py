# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.variable_presentation import VariablePresentation  # noqa: E501
from openapi_server.test import BaseTestCase


class TestVariablePresentationController(BaseTestCase):
    """VariablePresentationController integration test stubs"""

    def test_variablepresentations_get(self):
        """Test case for variablepresentations_get

        List all VariablePresentation entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/variablepresentations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
