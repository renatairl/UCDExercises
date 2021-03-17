import pandas as pd
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_width', 1000)

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")
