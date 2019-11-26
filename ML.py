import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Importing the dataset
dataset = pd.read_csv("WeatherDATA1.csv")
X = dataset.iloc[:, 4:7].values
y = dataset.iloc[:, 2].values

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)


print(pol_reg.predict(poly_reg.fit_transform([[25, 12, 2019]])))
