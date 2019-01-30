import pandas as pd

df = pd.read_csv("miso_output_2019_1_summary/summary/miso_output_2019_1.miso_summary", sep="\t")

f = open("miso_output_2019_1_summary/summary/miso_output_2019_1.miso_summary.parsed", "w")

f.write(df.sort_values(by=["miso_posterior_mean"]).head()

df = pd.read_csv("miso_output_2019_7_summary/summary/miso_output_2019_7.miso_summary", sep="\t")

f = open("miso_output_2019_7_summary/summary/miso_output_2019_7.miso_summary.parsed", "w")

f.write(df.sort_values(by=["miso_posterior_mean"]).head()

df = pd.read_csv("miso_output_2019_1control_summary/summary/miso_output_2019_1control.miso_summary", sep="\t")

f = open("miso_output_2019_1control_summary/summary/miso_output_2019_1control.miso_summary.parsed", "w")

f.write(df.sort_values(by=["miso_posterior_mean"]).head()

df = pd.read_csv("miso_output_2019_7contrl_summary/summary/miso_output_2019_7control.miso_summary", sep="\t")

f = open("miso_output_2019_7control_summary/summary/miso_output_2019_7control.miso_summary.parsed", "w")

f.write(df.sort_values(by=["miso_posterior_mean"]).head()
