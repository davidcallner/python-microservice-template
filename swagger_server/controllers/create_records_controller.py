import connexion
import six
from flask import Flask , request, render_template, jsonify

from swagger_server.models.record_model import RecordModel  # noqa: E501
from swagger_server import util


def create_record(body):  # noqa: E501
    """Creates a new record.

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [RecordModel.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
        req = request.get_json()
        print(req)
        return jsonify({'status': 'success', 'request': req})

