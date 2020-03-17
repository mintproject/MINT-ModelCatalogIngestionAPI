# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.visualization import Visualization  # noqa: E501
from openapi_server.test import BaseTestCase


class TestVisualizationController(BaseTestCase):
    """VisualizationController integration test stubs"""

    def test_visualizations_get(self):
        """Test case for visualizations_get

        List all Visualization entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/visualizations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
