# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.record_status import RecordStatus  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetStatusDataController(BaseTestCase):
    """GetStatusDataController integration test stubs"""

    def test_get_status(self):
        """Test case for get_status

        Gets all the status data
        """
        response = self.client.open(
            '//record/status',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
