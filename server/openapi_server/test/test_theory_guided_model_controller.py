# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.theory_guided_model import TheoryGuidedModel  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTheoryGuidedModelController(BaseTestCase):
    """TheoryGuidedModelController integration test stubs"""

    def test_theory_guidedmodels_get(self):
        """Test case for theory_guidedmodels_get

        List all Theory-GuidedModel entities
        """
        query_string = [('username', 'mint@isi.edu')]
                        
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.4.0/theory-guidedmodels',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
