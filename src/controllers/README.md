## Select Features

### Filter method
<!-- TODO -->

### Wrapper method
**URL**: http://localhost:8080/wrapperMethod/arima

**Method**: GET

**Response**:

> Input and output schemas and an example for each.

-------

**URL**: http://localhost:8080/wrapperMethod/arima

**Method**: POST

**Header**: Content-Type: application/json

**Body**:

```
{
    "dataDesc": {
        "data": [
            {
              "Working Electrode NO2": [
                    289.84, 288.77, 286.62, 284.81, 285.56, 
                    284.93, 285.36, 285.21, 284.95, 285.59, 
                    286.47, 287.07, 286.68, 286.91, 287.89, 
                    288.01, 287.73, 286.96, 288.85, 288.21
              ],
              "Auxiliar Electrode NO2": [
                    288.92, 288.44, 287.95, 286.8, 287.33, 
                    287.28, 287.05, 287.49, 287.25, 287.19, 
                    287.63, 287.82, 288.33, 288.2, 288.47, 
                    288.79, 289.24, 289.38, 289.97, 289.35
              ],
              "Temperature": [
                    13.59, 15.79, 17.87, 17.51, 17.27, 
                    17.87, 17.25, 17.42, 16.85, 15.21, 
                    13.9, 12.85, 12.34, 11.77, 10.89, 
                    10.33, 9.97, 9.69, 9.44, 9.95
              ],
              "Humidity": [
                    71.97, 65.39, 60.62, 59.97, 61.62, 
                    60.97, 62.77, 64.13, 65.76, 69.9, 
                    75.84, 79.46, 81.28, 82.11, 84.86, 
                    86.43, 88.02, 88.65, 89.52, 88.62
              ],
              "Pressure": [
                    1002.0, 1002.0, 1002.0, 1002.0, 1002.0, 
                    1002.0, 1002.0, 1002.0, 1002.0, 1002.0, 
                    1002.0, 1002.0, 1002.0, 1003.0, 1003.0, 
                    1003.0, 1003.0, 1003.0, 1003.0, 1003.0
              ]
            }
        ]
    },
    "options": {
        "attribute": "Pressure",
        "arOrder": 5,
        "iOrder": 1,
        "maOrder": 0
    }
}
```

**Response**:

```
{
    "attribute": "Pressure",
    "features": [
        "Working Electrode NO2"
    ],
    "metrics": {
        "meanAbsoluteError": 0.06339317392661523,
        "rootMeanSquareError": 0.19605223574986763
    }
}
```

-------

**URL**: http://localhost:8080/wrapperMethod/kmeans

**Method**: GET

**Response**:

> Input and output schemas and an example for each.

-------

**URL**: http://localhost:8080/wrapperMethod/kmeans

**Method**: POST

**Header**: Content-Type: application/json

**Body**:

```
{
    "dataDesc": {
        "data": [
            {
              "Working Electrode NO2": [
                    289.84, 288.77, 286.62, 284.81, 285.56, 
                    284.93, 285.36, 285.21, 284.95, 285.59, 
                    286.47, 287.07, 286.68, 286.91, 287.89, 
                    288.01, 287.73, 286.96, 288.85, 288.21
              ],
              "Auxiliar Electrode NO2": [
                    288.92, 288.44, 287.95, 286.8, 287.33, 
                    287.28, 287.05, 287.49, 287.25, 287.19, 
                    287.63, 287.82, 288.33, 288.2, 288.47, 
                    288.79, 289.24, 289.38, 289.97, 289.35
              ],
              "Temperature": [
                    13.59, 15.79, 17.87, 17.51, 17.27, 
                    17.87, 17.25, 17.42, 16.85, 15.21, 
                    13.9, 12.85, 12.34, 11.77, 10.89, 
                    10.33, 9.97, 9.69, 9.44, 9.95
              ],
              "Humidity": [
                    71.97, 65.39, 60.62, 59.97, 61.62, 
                    60.97, 62.77, 64.13, 65.76, 69.9, 
                    75.84, 79.46, 81.28, 82.11, 84.86, 
                    86.43, 88.02, 88.65, 89.52, 88.62
              ],
              "Pressure": [
                    1002.0, 1002.0, 1002.0, 1002.0, 1002.0, 
                    1002.0, 1002.0, 1002.0, 1002.0, 1002.0, 
                    1002.0, 1002.0, 1002.0, 1003.0, 1003.0, 
                    1003.0, 1003.0, 1003.0, 1003.0, 1003.0
              ]
            }
        ]
    },
    "options": {
        "nClusters": 3
    }
}
```

**Response**:

```
{
    "features": [
        "Working Electrode NO2",
        "Humidity"
    ],
    "silhouetteScore": 0.5366448278725782
}
```
    
## Clustering
##### Hierarchical
<!-- TODO -->