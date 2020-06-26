# coding: utf-8

from __future__ import absolute_import

import logging
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.person import Person  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPersonController(BaseTestCase):
    """PersonController integration test stubs"""
    logger = logging.getLogger("testing")
    
    def test_persons_get(self):
        """Test case for persons_get

        List all Person entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/persons',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.json)

    def test_persons_get_id_mint(self):
        """Test case for persons_get

        List all Person entities
        """
        query_string = [('username', 'mint@isi.edu')]

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/persons/{}'.format("khider_deborah"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_get_id_texas(self):
        """Test case for persons_get

        List all Person entities
        """
        query_string = [('username', 'texas@isi.edu')]

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/persons/{}'.format("khider_deborah"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_get_id_mint_not_found(self):
        """Test case for persons_get

        List all Person entities
        """
        query_string = [('username', 'mint@isi.edu')]

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/persons/{}'.format("b0b454fc-d77d-4778-9d37-6e327c00b0c2"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
