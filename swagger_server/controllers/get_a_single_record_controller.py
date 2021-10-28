import connexion
import six
from flask import jsonify
import json


from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def get_recordby_id(record_id):  # noqa: E501
    """Returns a record by ID.

     # noqa: E501

    :param record_id: The ID of the record to return.
    :type record_id: int

    :rtype: InlineResponse200
    """
    return jsonify({"data":record_id}), 200
