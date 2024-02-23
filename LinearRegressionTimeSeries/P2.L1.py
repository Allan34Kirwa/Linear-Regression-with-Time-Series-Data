from myFunction import df
# Add lag feature
# Add to my wrangle function to create a column called "P2.L1" 
# that contains the mean"P2" reading from the previous hour.
df["P2.L1"] = df["P2"].shift(1)

# Drop NaN row
df.dropna(inplace=True)

# The take these two to my wrangle function