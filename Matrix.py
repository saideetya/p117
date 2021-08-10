#Uploading the csv 
from google.colab import files
data_to_load = files.upload()

import pandas as pd

df = pd.read_csv("BankNote_Authentication")

print(df.head())


