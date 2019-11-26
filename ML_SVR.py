import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("WeatherDATA1.csv")
X = dataset.iloc[:, 4:7].values
y = dataset.iloc[:, 3].values

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y.reshape(-1, 1)

from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X, y)

y_pred = regressor.predict([[26, 11, 2019]])
print(y_pred)
