import matplotlib.pyplot as plt
from myFunction import df
# Create a scatter plot that shows PM 2.5 mean reading for each our as a function of the mean reading from the previous hour
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x=df["P2.L1"], y=df["P2"])
ax.plot([0, 120], [0, 120], linestyle="--", color="red")
plt.xlabel("P2.L1")
plt.ylabel("P2")
plt.title("PM2.5 Autocorrelation");