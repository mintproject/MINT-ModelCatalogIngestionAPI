# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.region import Region  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRegionController(BaseTestCase):
    """RegionController integration test stubs"""

    def test_regions_get(self):
        """Test case for regions_get

        List all Region entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/regions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.json)

    def test_id_get_circular(self):
        """Test case for test_id_get_circular
        Get a Region
        """

        resource_name = "Travis"
        resource_uri = "https://w3id.org/okn/i/mint/Travis"
        query_string = [('username', self.get_username)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/regions/{id}'.format(id=resource_name),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assertEqual(Region.from_dict(response.json).id, resource_uri)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
