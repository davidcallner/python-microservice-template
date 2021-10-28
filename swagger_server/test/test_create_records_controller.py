# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.record_model import RecordModel  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCreateRecordsController(BaseTestCase):
    """CreateRecordsController integration test stubs"""

    def test_create_record(self):
        """Test case for create_record

        Creates a new record.
        """
        body = [RecordModel()]
        response = self.client.open(
            '//records/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
