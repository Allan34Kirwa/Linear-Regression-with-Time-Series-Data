from myFunction import df
#  Split the DataFrame df into the feature matrix X and the target vector y. Your target is "P2"
target="P2"
y = df[target]
X = df.drop(columns=target)

len(X)
# Where the cutoff is
cutoff = int(len(X)*0.8)

X_train, y_train = X.iloc[:cutoff], y.iloc[:cutoff]
X_test, y_test = X.iloc[cutoff:], y.iloc[cutoff:]

X_test = X.iloc[:cutoff]
y_train = y.iloc[:cutoff]

X_test = X.iloc[cutoff:]
y_test = y.iloc[cutoff:]
