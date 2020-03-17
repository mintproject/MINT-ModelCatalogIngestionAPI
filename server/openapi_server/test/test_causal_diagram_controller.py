# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.causal_diagram import CausalDiagram  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCausalDiagramController(BaseTestCase):
    """CausalDiagramController integration test stubs"""

    def test_causaldiagrams_get(self):
        """Test case for causaldiagrams_get

        List all CausalDiagram entities
        """
        query_string = [('username', 'mint@isi.edu')]

        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/causaldiagrams',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
