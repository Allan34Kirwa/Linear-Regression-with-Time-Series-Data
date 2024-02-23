from sklearn.linear_model import LinearRegression
from LinearRegressionTimeSeries.split import X_train, y_train


# Instantiate a LinearRegression model named model, and fit it to your training data.
model = LinearRegression()
model.fit(X_train, y_train)