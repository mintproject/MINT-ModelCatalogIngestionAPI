# coding: utf-8

from __future__ import absolute_import

import logging
import unittest

from flask import json
from six import BytesIO

from openapi_server.models import Model
from openapi_server.test import BaseTestCase

MINT_USERNAME = "mint@isi.edu"

class TestModel(BaseTestCase):
    """Model integration test stubs"""
    logger = logging.getLogger("TestModel")
    def test_model_get_id(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/models/{}'.format("CYCLES"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assertIsInstance(Model.from_dict(response.json), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.json)


    def test_model_custom_index_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'flooding')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/custom/models/variable',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_model_custom_intervention_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'Fertilizer')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/custom/model/intervention',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_model_custom_region_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'baro')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/custom/model/region',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_model_custom_variable_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'crop')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/custom/models/variable',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_model_custom_standard_variable_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'crop')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/custom/models/standard_variable',
            method='GET',
            headers=headers,
            query_string=query_string)

        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
