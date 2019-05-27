import unittest

import pandas as pd

from src.services.wrapper_method_impl import WrapperMethodImpl


# noinspection SpellCheckingInspection
class TestWrapperMethodService(unittest.TestCase):

    def setUp(self):
        self.wrapper_method_service = WrapperMethodImpl('http://localhost:8081')

        df = pd.read_csv('../../resources/dataset.csv', delimiter=';', index_col=0)
        self.df_custom = df.reset_index().to_dict(orient='records')

    def test_wrapper_ARIMA_with_default_data(self):
        data = [{"month": "1-01", "sales": 266.0}, {"month": "1-02", "sales": 145.9}, {"month": "1-03", "sales": 183.1},
                {"month": "1-04", "sales": 119.3}, {"month": "1-05", "sales": 180.3}, {"month": "1-06", "sales": 168.5},
                {"month": "1-07", "sales": 231.8}, {"month": "1-08", "sales": 224.5}, {"month": "1-09", "sales": 192.8},
                {"month": "1-10", "sales": 122.9}, {"month": "1-11", "sales": 336.5}, {"month": "1-12", "sales": 185.9},
                {"month": "2-01", "sales": 194.3}, {"month": "2-02", "sales": 149.5}, {"month": "2-03", "sales": 210.1},
                {"month": "2-04", "sales": 273.3}, {"month": "2-05", "sales": 191.4}, {"month": "2-06", "sales": 287.0},
                {"month": "2-07", "sales": 226.0}, {"month": "2-08", "sales": 303.6}, {"month": "2-09", "sales": 289.9},
                {"month": "2-10", "sales": 421.6}, {"month": "2-11", "sales": 264.5}, {"month": "2-12", "sales": 342.3},
                {"month": "3-01", "sales": 339.7}, {"month": "3-02", "sales": 440.4}, {"month": "3-03", "sales": 315.9},
                {"month": "3-04", "sales": 439.3}, {"month": "3-05", "sales": 401.3}, {"month": "3-06", "sales": 437.4},
                {"month": "3-07", "sales": 575.5}, {"month": "3-08", "sales": 407.6}, {"month": "3-09", "sales": 682.0},
                {"month": "3-10", "sales": 475.3}, {"month": "3-11", "sales": 581.3}, {"month": "3-12", "sales": 646.9}]

        result = self.wrapper_method_service.wrapper_arima(data=data, features=['month'], attribute='sales',
                                                           ar_order=5, i_order=1, ma_order=0)
        self.assertEqual(result, {'features': ['month'], 'attribute': 'sales',
                                  'metrics': {'meanAbsoluteError': 52.727268403460535,
                                              'rootMeanSquareError': 67.37697003924217}})

    def test_wrapper_ARIMA_with_custom_data(self):
        data = self.df_custom
        columns = ['Time', 'Working Electrode NO2', 'Auxiliar Electrode NO2', 'Working Electrode O3',
                   'Auxiliar Electrode O3', 'Working electrode CO', 'Auxiliar electrode CO', 'Working Electrode SO2',
                   'Auxiliar Electrode SO2', 'Humidity', 'Pressure']

        result = self.wrapper_method_service.wrapper_arima(data=data, features=columns, attribute='Temperature',
                                                           ar_order=5, i_order=1, ma_order=0)
        self.assertEqual(result, {'features': ['Time'], 'attribute': 'Temperature',
                                  'metrics': {'meanAbsoluteError': 0.7036582220175591,
                                              'rootMeanSquareError': 1.1504588872321118}})

    def test_wrapper_KMEANS_with_default_data(self):
        data = [{"x": 20.3338847898911, "y": 70.9608018911035}, {"x": 26.5165713494385, "y": 46.4862383887838},
                {"x": 22.5405564503676, "y": 68.9679382342013}, {"x": 29.9393973268233, "y": 43.4853462432036},
                {"x": 13.05480068866, "y": 76.3221641119346}, {"x": 25.2384254905452, "y": 68.9133633755761},
                {"x": 23.1553508372478, "y": 60.8484183471996}, {"x": 34.7867591608082, "y": 62.374536303667},
                {"x": 35.4109048886794, "y": 58.8987189980316}, {"x": 38.5175405140372, "y": 56.1424244109387},
                {"x": 97.1865108432285, "y": 79.0764314181978}, {"x": 68.0550425292563, "y": 68.7145731834059},
                {"x": 76.9587226195596, "y": 84.0134969582564}, {"x": 77.8924457763679, "y": 94.2337408933988},
                {"x": 95.1270061424319, "y": 81.5486319091794}, {"x": 60.3422905089889, "y": 75.1475592989026},
                {"x": 97.8872293428121, "y": 102.366600071028}, {"x": 75.6921793935179, "y": 82.1061642879839},
                {"x": 90.3069726352579, "y": 75.0050125673137}, {"x": 85.812705720906, "y": 86.1304198438951}]

        result = self.wrapper_method_service.wrapper_kmeans(data=data, features=['x', 'y'], n_clusters=2)
        self.assertEqual(result, {'attributes': ['x'], 'silhouetteScore': 0.764255970646213})

    def test_wrapper_KMEANS_with_custom_data(self):
        data = self.df_custom
        columns = ['Working Electrode NO2', 'Auxiliar Electrode NO2', 'Working Electrode O3',
                   'Auxiliar Electrode O3', 'Working electrode CO', 'Auxiliar electrode CO', 'Working Electrode SO2',
                   'Auxiliar Electrode SO2', 'Temperature', 'Humidity', 'Pressure']

        result = self.wrapper_method_service.wrapper_kmeans(data=data, features=columns, n_clusters=2)
        self.assertEqual(result, {'attributes': ['Working Electrode NO2', 'Working electrode CO'],
                                  'silhouetteScore': 0.5670080371248948})
