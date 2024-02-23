import matplotlib.pyplot as plt
from myFunction import df
df["P2"].rolling(168).mean().isnull().sum()

# Rolling Averages
df["P2"].rolling(168).mean()

# Plotting my rolling averages of the "P2" readings in df
fig, ax = plt.subplots(figsize=(15, 6))
df["P2"].rolling(168).mean().plot(ax=ax, ylabel="PM2.5", title="Weekly Rolling Average");