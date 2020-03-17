# coding: utf-8

from __future__ import absolute_import

import logging
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: E501
from openapi_server.test import BaseTestCase

MINT_USERNAME = "mint@isi.edu"

class TestModelConfigurationSetupController(BaseTestCase):
    """ModelConfigurationSetupController integration test stubs"""
    logger = logging.getLogger("TestModelConfigurationSetupController")

    def test_modelconfigurationsetups_get(self):
        """Test case for modelconfigurationsetups_get

        List all ModelConfigurationSetup entities
        """
        query_string = [('username', MINT_USERNAME)]

        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/modelconfigurationsetups',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assertTrue(response.json)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_id_get(self):
        """Test case for modelconfigurationsetups_id_get

        Get a ModelConfigurationSetup
        """
        query_string = [('username', MINT_USERNAME)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/modelconfigurationsetups/{id}'.format(id='hand_v2_travis'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assertTrue(response.json)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_custom_id_get(self):
        """Test case for modelconfigurationsetups_id_get

        Get a ModelConfigurationSetup
        """
        query_string = [('username', MINT_USERNAME)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/custom/modelconfigurationsetups/{id}'.format(id='hand_v2_travis'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assertTrue(response.json)
        resource = ModelConfigurationSetup.from_dict(response.json)
        self.assertTrue(resource.has_input)
        self.assertTrue(resource.has_output)
        self.assertTrue(resource.has_parameter)
        self.assertTrue(resource.has_input[0].has_fixed_resource)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurationsetups_custom_variable(self):
        """Test case for modelconfigurationsetups_id_get

        Get a ModelConfigurationSetup
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'flood')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/custom/modelconfigurationsetups/variable',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assertTrue(response.json)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
