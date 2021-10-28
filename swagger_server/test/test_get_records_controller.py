# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.record_status import RecordStatus  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetRecordsController(BaseTestCase):
    """GetRecordsController integration test stubs"""

    def test_get_record(self):
        """Test case for get_record

        Gets all the records
        """
        response = self.client.open(
            '//records',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
