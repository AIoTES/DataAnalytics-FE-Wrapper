import unittest

import pandas as pd

from src.services.data_lake_service import QueryDataLake


class TestDataDescStructure(unittest.TestCase):

    def setUp(self):
        self.service = QueryDataLake()

    def test_no_expression(self):
        data = {
            "data": [
                {"coords": [5.1, 3.5, 1.4, 0.2]},
                {"coords": [5.8, 4.0, 1.2, 0.2]},
                {"coords": [5.7, 4.4, 1.5, 0.4]},
                {"coords": [5.4, 3.9, 1.3, 0.4]},
                {"coords": [5.1, 3.5, 1.4, 0.3]},
                {"coords": [5.7, 3.8, 1.7, 0.3]},
                {"coords": [5.1, 3.8, 1.5, 0.3]},
                {"coords": [5.4, 3.4, 1.7, 0.2]},
                {"coords": [5.1, 3.7, 1.5, 0.4]},
                {"coords": [4.6, 3.6, 1.0, 0.2]}
            ]
        }
        actual = self.service.retrieve_data_as_data_frame(data)
        expected = pd.DataFrame(data["data"])
        print(actual)
        self.assertTrue(expected.equals(actual))

    def test_no_expression_dict(self):
        data = {
            "data": [
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]}
            ]
        }
        actual = self.service.retrieve_data_as_data_frame(data)
        expected = pd.DataFrame.from_dict(data["data"][0])
        print(actual)
        self.assertTrue(expected.equals(actual))

    def test_simple_expression(self):
        data = {
            "data": [
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]}
            ],
            "expression": "temp"
        }

        data_expected = [
            {"temp": [1, 2, 3, 4]},
            {"temp": [1, 2, 3, 4]},
            {"temp": [1, 2, 3, 4]},
            {"temp": [1, 2, 3, 4]},
            {"temp": [1, 2, 3, 4]}
        ]

        actual = self.service.retrieve_data_as_data_frame(data)
        expected = pd.DataFrame(data_expected)
        print(actual)
        self.assertTrue(expected.equals(actual))

    def test_multiply_expresion(self):
        data = {
            "data": [
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]}
            ],
            "expression": "temp * humd"
        }

        data_expected = [
            {"result": [4, 6, 6, 4]},
            {"result": [4, 6, 6, 4]},
            {"result": [4, 6, 6, 4]},
            {"result": [4, 6, 6, 4]},
            {"result": [4, 6, 6, 4]}
        ]

        actual = self.service.retrieve_data_as_data_frame(data)
        expected = pd.DataFrame(data_expected)
        print(actual)
        self.assertTrue(expected.equals(actual))

    def test_divide_expression(self):
        data = {
            "data": [
                {"temp": [8, 6, 4, 2], "humd": [4, 3, 2, 1]},
                {"temp": [8, 6, 4, 2], "humd": [4, 3, 2, 1]},
                {"temp": [8, 6, 4, 2], "humd": [4, 3, 2, 1]},
                {"temp": [8, 6, 4, 2], "humd": [4, 3, 2, 1]},
                {"temp": [8, 6, 4, 2], "humd": [4, 3, 2, 1]},
            ],
            "expression": "temp / humd"
        }

        data_expected = [
            {"result": [2, 2, 2, 2]},
            {"result": [2, 2, 2, 2]},
            {"result": [2, 2, 2, 2]},
            {"result": [2, 2, 2, 2]},
            {"result": [2, 2, 2, 2]}
        ]

        actual = self.service.retrieve_data_as_data_frame(data)
        expected = pd.DataFrame(data_expected)
        print(actual)
        self.assertTrue(expected.equals(actual))

    def test_add_expression(self):
        data = {
            "data": [
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
            ],
            "expression": "temp + humd"
        }
        data_expected = [
            {"result": [5, 5, 5, 5]},
            {"result": [5, 5, 5, 5]},
            {"result": [5, 5, 5, 5]},
            {"result": [5, 5, 5, 5]},
            {"result": [5, 5, 5, 5]}
        ]

        actual = self.service.retrieve_data_as_data_frame(data)
        expected = pd.DataFrame(data_expected)
        print(actual)
        self.assertTrue(expected.equals(actual))

    def test_subtract_expression(self):
        data = {
            "data": [
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
                {"temp": [1, 2, 3, 4], "humd": [4, 3, 2, 1]},
            ],
            "expression": "temp - humd"
        }
        data_expected = [
            {"result": [-3, -1, 1, 3]},
            {"result": [-3, -1, 1, 3]},
            {"result": [-3, -1, 1, 3]},
            {"result": [-3, -1, 1, 3]},
            {"result": [-3, -1, 1, 3]}
        ]

        actual = self.service.retrieve_data_as_data_frame(data)
        expected = pd.DataFrame(data_expected)
        print(actual)
        self.assertTrue(expected.equals(actual))

# "dataDesc": {
#     "type": "object",
#     "properties": {
#         "data": {
#             "type": "array",
#             "description": "The data to be processed, as an array of records (JSON objects). Either this property or 'query' should be used in a dataDesc.",
#             "items": {"type": "object"}
#         },
#         "query": {
#             "type": "string",
#             "description": "A query to the SIL data model, whose results are the data to be processed. Either this property or 'data' should be used in a dataDesc."
#         },
#         "expression": {
#             "type": "string",
#             "description": "An expression of the data record attributes, whose result is to be used as the input for data processing."
#         }
#     }
# }
