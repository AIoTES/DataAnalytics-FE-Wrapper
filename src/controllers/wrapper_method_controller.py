import json
import logging

import requests
from flask import Blueprint, request, Response

import src.utils.utils as utils
from src.services.data_lake_service import QueryDataLake
from src.services.wrapper_method_service import WrapperMethod

api = Blueprint('wrapperMethod_controller', __name__)
# noinspection PyTypeChecker
wrapperMethod: WrapperMethod = None
# noinspection PyTypeChecker
queryDataLake: QueryDataLake = None


# noinspection SpellCheckingInspection,PyPep8Naming
@api.route('/arima', methods=['GET', 'POST'])
def wrapper_ARIMA():
    if request.method == 'GET':
        with open('./controllers/schemas/arima_schema.json') as f:
            return Response(response=json.dumps(json.load(f), sort_keys=False, separators=(',', ':')),
                            content_type="application/json", status=200)

    if request.method == 'POST':
        data = request.get_json() or {}

        if not data:
            logging.error("{}:{}".format("ContentLengthRequired", "Zero/No Content-Length"))
            return utils.error_response(411, "Zero/No Content-Length")

        if 'dataDesc' not in list(data.keys()) or 'options' not in list(data.keys()):
            logging.error("{}:{}".format("Bad Request", "JSON Incomplete"))
            return utils.bad_request("JSON incomplete. {} fields are necessary".format(['dataDesc', 'options']))

        if 'attribute' not in list(data['options'].keys()):
            logging.error("{}:{}".format("Bad Request", "JSON Incomplete"))
            return utils.bad_request("JSON incomplete. {} field are necessary".format(['attribute']))

        if not data.get('forward', True):
            logging.error("{}:{}".format("Not Implemented", "Only the selection of Step Forward functions "
                                                            "is supported at the moment."))
            return utils.error_response(501, "Not Implemented")

        attribute = data['options'].pop('attribute')
        options = {
            'ar_order': data['options'].get('arOrder', 1),
            'i_order': data['options'].get('iOrder', 1),
            'ma_order': data['options'].get('maOrder', 0)
        }

        df = queryDataLake.retrieve_data_as_data_frame(data['dataDesc'])

        if attribute not in list(df.columns.values):
            logging.error("{}:{}".format("Bad Request", "Input JSON error"))
            return utils.bad_request("Input JSON error. The value {} "
                                     "in {} field is wrong".format([attribute], ['attribute']))

        features = list(df.columns.values)
        features.remove(attribute)

        try:
            message = wrapperMethod.wrapper_arima(df, features=features, attribute=attribute, **options)
            return Response(response=json.dumps(message, sort_keys=True, separators=(',', ':')),
                            content_type="application/json", status=200)
        except requests.exceptions.ConnectionError:
            return utils.error_response(500, 'Unreachable Data Analystics Server')


# noinspection SpellCheckingInspection,PyPep8Naming
@api.route('/kmeans', methods=['GET', 'POST'])
def wrapper_KMEANS():
    if request.method == 'GET':
        with open('./controllers/schemas/kmeans_schema.json') as f:
            return Response(response=json.dumps(json.load(f), sort_keys=False, separators=(',', ':')),
                            content_type="application/json", status=200)

    if request.method == 'POST':
        data = request.get_json() or {}

        if not data:
            logging.error("{}:{}".format("ContentLengthRequired", "Zero/No Content-Length"))
            return utils.error_response(411, "Zero/No Content-Length")

        if 'dataDesc' not in list(data.keys()):  # or 'options' not in list(data.keys()):
            logging.error("{}:{}".format("Bad Request", "JSON Incomplete"))
            return utils.bad_request("JSON incomplete. {} field is necessary".format(['dataDesc']))

        if not data.get('forward', True):
            logging.error("{}:{}".format("Not Implemented", "Only the selection of Step Forward functions "
                                                            "is supported at the moment"))
            return utils.error_response(501, "Not Implemented")

        n_clusters = data.get('options', {}).pop('nClusters', 2)

        df = queryDataLake.retrieve_data_as_data_frame(data['dataDesc'])
        features = list(df.columns.values)

        try:
            message = wrapperMethod.wrapper_kmeans(df, features=features, n_clusters=n_clusters)
            return Response(response=json.dumps(message, sort_keys=True, separators=(',', ':')),
                            content_type="application/json", status=200)
        except requests.exceptions.ConnectionError:
            return utils.error_response(500, 'Unreachable Data Analystics Server')
