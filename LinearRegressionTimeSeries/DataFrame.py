import pandas as pd
from LinearRegressionTimeSeries.split import y_test, model, X_test

# Create a DataFrame from a dictionary using pandas
df_pred_test = pd.DataFrame(
    {
        "y_test": y_test,
        "y_pred": model.predict(X_test)
    }  
)
df_pred_test.head()