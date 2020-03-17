# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.point_based_grid import PointBasedGrid  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPointBasedGridController(BaseTestCase):
    """PointBasedGridController integration test stubs"""

    def test_pointbasedgrids_get(self):
        """Test case for pointbasedgrids_get

        List all PointBasedGrid entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/pointbasedgrids',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
