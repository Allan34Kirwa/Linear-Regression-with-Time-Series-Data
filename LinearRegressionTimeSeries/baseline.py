from sklearn.metrics import mean_absolute_error
from split import X_train, y_train
from LinearRegressionTimeSeries.split import X_train
# Calculate the baseline mean absolute error for my model.
y_mean = y_train.mean()
y_pred_baseline = [y_mean] * len(y_train)
mae_baseline = mean_absolute_error(y_train, y_pred_baseline)

print("Mean P2 Reading:", round(y_train.mean(), 2))
print("Baseline MAE:", round(mae_baseline, 2))

# Sample output (Mean P2 Reading: 9.27 & Baseline MAE: 3.89)
