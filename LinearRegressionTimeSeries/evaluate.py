from sklearn.metrics import mean_absolute_error
from LinearRegressionTimeSeries.split import X_train, y_train, model, y_test, X_test

# Calculate the training and test mean absolute error for your model.
training_mae = mean_absolute_error(y_train, model.predict(X_train))
test_mae = mean_absolute_error(y_test, model.predict(X_test))
print("Training MAE:", round(training_mae, 2))
print("Test MAE:", round(test_mae, 2))