# noinspection SpellCheckingInspection
class WrapperMethod:

    def __init__(self, analytics_server):
        self.analytics_server = analytics_server

    def wrapper_arima(self, data, features, attribute, ar_order, i_order, ma_order):
        raise NotImplementedError('You must implement this method')

    def wrapper_kmeans(self, data, features, n_clusters):
        raise NotImplementedError('You must implement this method')
