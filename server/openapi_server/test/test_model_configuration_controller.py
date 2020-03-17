# coding: utf-8

from __future__ import absolute_import

import logging
import unittest
from pathlib import Path

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase
from openapi_server.test.utils import read_json_file

from openapi_server.models.model_configuration import ModelConfiguration

INPUT_TESTS_DIRECTORY = Path('.') / 'openapi_server' / 'test' / 'input_tests'

class TestModelConfigurationController(BaseTestCase):
    logger = logging.getLogger("TestModelConfigurationController")
    input_test_directory = Path(__file__).parent / "input_tests"

    """ModelConfigurationController integration test stubs"""
    def test_modelconfigurations_get(self):
        """Test case for modelconfigurations_get

        List all ModelConfiguration entities
        """
        query_string = [('username', self.get_username),
                        ('label', 'agriculture')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/modelconfigurations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_id_get(self):
        """Test case for modelconfigurations_id_get
        Get a ModelConfiguration
        """
        query_string = [('username', self.get_username)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/modelconfigurations/{id}'.format(id="hand_v2"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modelconfigurations_without_id_post(self):
        input_file_path = self.input_test_directory / "model_configuration_without_id.json"
        token_ = self.login()["access_token"]
        data = read_json_file(input_file_path)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(token_),
        }
        response = self.client.open(
            '/v1.4.0/modelconfigurations',
            method='POST',
            headers=headers,
            data=json.dumps(data),
            content_type='application/json')

        self.assertEqual(response.status_code, 201)
        model_request = ModelConfiguration.from_dict(data)
        model_request.id = response.json['id']

        # ##### Verify if the request and response are equals
        # verification_query_string = [('username', "mosorio@isi.edu")]
        # verification_response = self.client.open(
        #     '/v1.4.0/modelconfigurations/{id}'.format(id=model_request.id),
        #     method='GET',
        #     headers=headers,
        #     query_string=verification_query_string)
        # model_response = ModelConfiguration.from_dict(verification_response.json)
        # self.logger.warning(model_response)
        # self.assertEqual(model_request, model_response)


if __name__ == '__main__':
    unittest.main()
