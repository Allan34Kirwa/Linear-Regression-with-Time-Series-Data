import pandas as pd
def wrangle(collection):
    results = collection.find(
        {"metadata.site": 29, "metadata.measurement": "P2"},
        projection={"P2": 1, "timestamp": 1, "_id": 0},
    )

    df = pd.DataFrame(results).set_index("timestamp")
    
    # Localize timezone
    df.index = df.index.tz_localize("UTC").tz_convert("Africa/Nairobi")
    
    # Remove outliers 
    df = df[df["P2"] < 500]
    
    # Resample to 1H window , ffill missing values
    df = df["P2"].resample("1H").mean().fillna(method="ffill").to_frame()
    
    #Add lag feature
    df["P2.L1"] = df["P2"].shift(1)
    
    # Drop NaN row
    df.dropna(inplace=True)
    
    return df