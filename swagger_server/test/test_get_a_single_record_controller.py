# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetASingleRecordController(BaseTestCase):
    """GetASingleRecordController integration test stubs"""

    def test_get_recordby_id(self):
        """Test case for get_recordby_id

        Returns a record by ID.
        """
        response = self.client.open(
            '//records/{recordId}'.format(record_id=2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
