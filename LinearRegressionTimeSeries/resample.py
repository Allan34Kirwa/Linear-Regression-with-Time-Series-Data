from myFunction import df

# Adding to my wrangle function to resample df to provide the mean "P2" reading for each hour
df["P2"].resample("1H").mean().head()

# Test cell for checking missing values
df["P2"].resample("1H").mean().isnull().sum()

# Therefore 102 is number of our missing values
# Test cell let's use forward fill
df["P2"].resample("1H").mean().fillna(method="ffill").to_frame().head()

# Let me take it to my wrangle function