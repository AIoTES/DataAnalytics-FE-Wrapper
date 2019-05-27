import logging

import pandas as pd


# noinspection SpellCheckingInspection
class QueryDataLake:

    @staticmethod
    def retrieve_data_as_data_frame(data_desc):
        if "query" in data_desc:
            logging.error("Query to data lake not implemented returning "
                          "default values. Query: {}".format(data_desc["query"]))
            return pd.read_csv('../resources/dataset.csv', delimiter=';', index_col=0)

        if "expression" in data_desc:
            expression_splitted = data_desc["expression"].split()
            if len(expression_splitted) == 1:
                for element in data_desc["data"]:
                    delete = [key for key in element if key != expression_splitted[0]]
                    for key in delete:
                        del element[key]

            else:
                for element in data_desc["data"]:
                    result = []
                    for x in range(0, len(element[expression_splitted[0]])):
                        if expression_splitted[1] == '*':
                            result.append(element[expression_splitted[0]][x] * element[expression_splitted[2]][x])
                        elif expression_splitted[1] == '/':
                            result.append(element[expression_splitted[0]][x] / element[expression_splitted[2]][x])
                        elif expression_splitted[1] == '+':
                            result.append(element[expression_splitted[0]][x] + element[expression_splitted[2]][x])
                        elif expression_splitted[1] == '-':
                            result.append(element[expression_splitted[0]][x] - element[expression_splitted[2]][x])

                    element["result"] = result

                for element in data_desc["data"]:
                    delete = [key for key in element if key != "result"]
                    for key in delete:
                        del element[key]

        if len(data_desc["data"]) == 1:
            df_response = pd.DataFrame.from_dict(data_desc["data"][0])
        else:
            expression_splitted = data_desc["expression"].split()
            if len(expression_splitted) == 1:

                df_response = [data_desc["data"][0][expression_splitted[0]]]
                for x in range(1, len(data_desc["data"])):
                    df_response = pd.np.concatenate((df_response, [data_desc["data"][x][expression_splitted[0]]]))
            else:
                df_response = [data_desc["data"][0]["result"]]
                for x in range(1, len(data_desc["data"])):
                    df_response = pd.np.concatenate((df_response, [data_desc["data"][x]["result"]]))

        return df_response
