from LinearRegressionTimeSeries.iterate import model
# Extract the intercept and coefficient from my model
intercept =  model.intercept_.round(2)
coefficient =  model.coef_.round(2)[0]
print(f"P2 = {intercept} + ({coefficient} * P2.L1)")

# Output is (P2 = 3.36 + (0.64 * P2.L1))