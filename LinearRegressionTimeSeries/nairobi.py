# Shape of `Nairobi`
import pandas as pd
from myFunction import wrangle  # Replace 'first_file_name' with the actual name of the first file
from client import nairobi
df = wrangle(nairobi)
print(df.shape)
df.head(10)