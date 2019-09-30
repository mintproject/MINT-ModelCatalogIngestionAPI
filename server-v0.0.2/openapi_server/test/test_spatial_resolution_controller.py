# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.spatial_resolution import SpatialResolution  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSpatialResolutionController(BaseTestCase):
    """SpatialResolutionController integration test stubs"""

    def test_spatialresolutions_get(self):
        """Test case for spatialresolutions_get

        List all SpatialResolution entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/spatialresolutions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spatialresolutions_id_delete(self):
        """Test case for spatialresolutions_id_delete

        Delete a SpatialResolution
        """
        headers = { 
        }
        response = self.client.open(
            '/v1.0.0/spatialresolutions/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spatialresolutions_id_get(self):
        """Test case for spatialresolutions_id_get

        Get a SpatialResolution
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/spatialresolutions/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spatialresolutions_id_put(self):
        """Test case for spatialresolutions_id_put

        Update a SpatialResolution
        """
        spatial_resolution = {
  "id" : [ "id", "id" ],
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/spatialresolutions/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(spatial_resolution),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spatialresolutions_post(self):
        """Test case for spatialresolutions_post

        Create a SpatialResolution
        """
        spatial_resolution = {
  "id" : [ "id", "id" ],
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/spatialresolutions',
            method='POST',
            headers=headers,
            data=json.dumps(spatial_resolution),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()