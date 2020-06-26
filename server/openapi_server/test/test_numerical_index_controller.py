# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.numerical_index import NumericalIndex  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNumericalIndexController(BaseTestCase):
    """NumericalIndexController integration test stubs"""

    def test_numericalindexs_get(self):
        """Test case for numericalindexs_get

        List all NumericalIndex entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/numericalindexs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.json)


if __name__ == '__main__':
    unittest.main()
