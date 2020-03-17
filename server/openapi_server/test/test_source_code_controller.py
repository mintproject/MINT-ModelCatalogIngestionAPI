# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.source_code import SourceCode  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSourceCodeController(BaseTestCase):
    """SourceCodeController integration test stubs"""

    def test_sourcecodes_get(self):
        """Test case for sourcecodes_get

        List all SourceCode entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/sourcecodes',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
