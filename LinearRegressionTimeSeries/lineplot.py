import matplotlib.pyplot as plt
from myFunction import df

#  Create a time series plot of the "P2" readings in df
fig, ax = plt.subplots(figsize=(15, 6))
df["P2"].plot(xlabel="Time", ylabel="PM2.5", title="PM2.5 Time Series", ax=ax);
