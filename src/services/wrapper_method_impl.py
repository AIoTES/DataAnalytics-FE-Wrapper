import requests

from src.services.wrapper_method_service import WrapperMethod


# noinspection SpellCheckingInspection
class WrapperMethodImpl(WrapperMethod):

    def wrapper_arima(self, data, features, attribute, ar_order, i_order, ma_order):
        url = self.analytics_server + '/arimatrain'
        body = {"options": {"attribute": attribute, "arOrder": ar_order, "iOrder": i_order, "maOrder": ma_order}}

        l_features = []
        best_mae = float("inf")
        best_rmse = float("inf")

        for feature in features:
            l_features.append(feature)
            body["data"] = data[l_features + [attribute]].to_dict(orient='records')

            response = requests.post(url, json=body, headers={"Content-Type": "application/json"}).json()
            metrics = response.get('fitMetrics')

            if metrics.get('MeanAbsoluteError') < best_mae and metrics.get('RootMeanSquareError') < best_rmse:
                best_mae = metrics.get('MeanAbsoluteError')
                best_rmse = metrics.get('RootMeanSquareError')
            else:
                l_features.pop()

        return {"features": l_features, "attribute": attribute, "metrics": {"meanAbsoluteError": best_mae,
                                                                            "rootMeanSquareError": best_rmse}}

    def wrapper_kmeans(self, data, features, n_clusters):
        url = self.analytics_server + '/kmeans'
        body = {"data": data.to_dict(orient='records'), "options": {"attributes": [], "nClusters": n_clusters,
                                                                    "extraInfo": True}}

        best_score = float("-inf")

        for feature in features:
            body["options"]["attributes"].append(feature)
            response = requests.post(url, json=body, headers={"Content-Type": "application/json"}).json()

            if response.get('silhouetteScore') > best_score:
                best_score = response.get('silhouetteScore')
            else:
                body["options"]["attributes"].pop()

        return {"features": body["options"]["attributes"], "silhouetteScore": best_score}
