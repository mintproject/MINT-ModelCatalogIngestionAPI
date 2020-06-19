# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.svo_variable import SVOVariable  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSVOVariableController(BaseTestCase):
    """SVOVariableController integration test stubs"""

    def test_svovariables_get(self):
        """Test case for svovariables_get

        List all instances of SVOVariable
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/svovariables',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_svovariables_id_delete(self):
        """Test case for svovariables_id_delete

        Delete an existing SVOVariable
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/svovariables/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_svovariables_id_get(self):
        """Test case for svovariables_id_get

        Get a single SVOVariable by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/svovariables/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_svovariables_id_put(self):
        """Test case for svovariables_id_put

        Update an existing SVOVariable
        """
        svo_variable = {
  "description" : [ "description", "description" ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/svovariables/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(svo_variable),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_svovariables_post(self):
        """Test case for svovariables_post

        Create one SVOVariable
        """
        svo_variable = {
  "description" : [ "description", "description" ],
  "id" : "id",
  "label" : [ "label", "label" ],
  "type" : [ "type", "type" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/svovariables'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(svo_variable),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
