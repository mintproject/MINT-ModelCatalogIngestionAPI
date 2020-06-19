# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.subsidy import Subsidy  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSubsidyController(BaseTestCase):
    """SubsidyController integration test stubs"""

    def test_subsidys_get(self):
        """Test case for subsidys_get

        List all instances of Subsidy
        """
        query_string = [('username', 'username_example'),
                        ('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/subsidys',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subsidys_id_delete(self):
        """Test case for subsidys_id_delete

        Delete an existing Subsidy
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1.5.0/subsidys/{id}'.format(id='id_example', user='user_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subsidys_id_get(self):
        """Test case for subsidys_id_get

        Get a single Subsidy by its id
        """
        query_string = [('username', 'username_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/subsidys/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subsidys_id_put(self):
        """Test case for subsidys_id_put

        Update an existing Subsidy
        """
        subsidy = {
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
            '/v1.5.0/subsidys/{id}'.format(id='id_example', user='user_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(subsidy),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subsidys_post(self):
        """Test case for subsidys_post

        Create one Subsidy
        """
        subsidy = {
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
            '/v1.5.0/subsidys'.format(user='user_example'),
            method='POST',
            headers=headers,
            data=json.dumps(subsidy),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
