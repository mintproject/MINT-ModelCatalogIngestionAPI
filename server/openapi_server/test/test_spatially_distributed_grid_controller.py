# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.spatially_distributed_grid import SpatiallyDistributedGrid  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSpatiallyDistributedGridController(BaseTestCase):
    """SpatiallyDistributedGridController integration test stubs"""

    def test_spatiallydistributedgrids_get(self):
        """Test case for spatiallydistributedgrids_get

        List all SpatiallyDistributedGrid entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/spatiallydistributedgrids',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        self.assertTrue(response.json)

if __name__ == '__main__':
    unittest.main()
