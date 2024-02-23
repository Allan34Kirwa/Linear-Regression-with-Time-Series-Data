# boxplot of the "P2" readings in df
import matplotlib.pyplot as plt
from myFunction import df
fig, ax = plt.subplots(figsize=(15, 6))
df["P2"].plot(kind="box", vert=False, title="Distribution of PM2.5 Readings", ax=ax);