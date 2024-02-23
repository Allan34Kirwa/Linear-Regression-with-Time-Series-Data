import plotly.express as px
from LinearRegressionTimeSeries.DataFrame import df_pred_test

# Create a time series line plot for the values in test_predictions using plotly express.
fig = px.line(df_pred_test, labels={"values":"P2"})
fig.show()