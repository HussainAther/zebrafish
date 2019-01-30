import pandas as pd

df = pd.read_csv("miso_output_2019_1_summary/summary/miso_output_2019_1.miso_summary", sep="\t")

print(df.head())

