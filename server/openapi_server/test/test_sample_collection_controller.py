# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.sample_collection import SampleCollection  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSampleCollectionController(BaseTestCase):
    """SampleCollectionController integration test stubs"""

    def test_samplecollections_get(self):
        """Test case for samplecollections_get

        List all SampleCollection entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/samplecollections',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
