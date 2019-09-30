# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.hybrid_model import HybridModel  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHybridModelController(BaseTestCase):
    """HybridModelController integration test stubs"""

    def test_hybridmodels_get(self):
        """Test case for hybridmodels_get

        List all HybridModel entities
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/hybridmodels',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hybridmodels_id_delete(self):
        """Test case for hybridmodels_id_delete

        Delete a HybridModel
        """
        headers = { 
        }
        response = self.client.open(
            '/v1.0.0/hybridmodels/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hybridmodels_id_get(self):
        """Test case for hybridmodels_id_get

        Get a HybridModel
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/hybridmodels/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hybridmodels_id_put(self):
        """Test case for hybridmodels_id_put

        Update a HybridModel
        """
        hybrid_model = {
  "hasGrid" : [ {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : [ "id", "id" ]
  }, {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : [ "id", "id" ]
  } ],
  "hasExplanationDiagram" : [ "{}", "{}" ],
  "hasEquation" : [ {
    "id" : [ "id", "id" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "id" : [ "id", "id" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "id" : [ "id", "id" ],
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ]
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/hybridmodels/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(hybrid_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hybridmodels_post(self):
        """Test case for hybridmodels_post

        Create a HybridModel
        """
        hybrid_model = {
  "hasGrid" : [ {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : [ "id", "id" ]
  }, {
    "hasDimensionality" : [ 0.8008281904610115, 0.8008281904610115 ],
    "hasFormat" : [ "hasFormat", "hasFormat" ],
    "hasFileStructure" : "{}",
    "hasPresentation" : [ "{}", "{}" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ],
    "hasFixedResource" : [ "{}", "{}" ],
    "hasSpatialResolution" : [ "hasSpatialResolution", "hasSpatialResolution" ],
    "hasCoordinateSystem" : [ "hasCoordinateSystem", "hasCoordinateSystem" ],
    "hasShape" : [ "hasShape", "hasShape" ],
    "hasDimension" : [ "hasDimension", "hasDimension" ],
    "position" : [ 6.027456183070403, 6.027456183070403 ],
    "id" : [ "id", "id" ]
  } ],
  "hasExplanationDiagram" : [ "{}", "{}" ],
  "hasEquation" : [ {
    "id" : [ "id", "id" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  }, {
    "id" : [ "id", "id" ],
    "label" : [ "label", "label" ],
    "type" : [ "type", "type" ]
  } ],
  "id" : [ "id", "id" ],
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ],
  "hasModelCategory" : [ "hasModelCategory", "hasModelCategory" ]
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1.0.0/hybridmodels',
            method='POST',
            headers=headers,
            data=json.dumps(hybrid_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()