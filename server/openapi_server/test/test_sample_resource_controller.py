# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.sample_resource import SampleResource  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSampleResourceController(BaseTestCase):
    """SampleResourceController integration test stubs"""

    def test_sampleresources_get(self):
        """Test case for sampleresources_get

        List all SampleResource entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.5.0/sampleresources',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        self.assertTrue(response.json)

if __name__ == '__main__':
    unittest.main()
