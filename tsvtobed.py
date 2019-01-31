import pandas as pd

df = pd.DataFrame.from_csv("summary_miso_output_2019_1/summary/miso_output_2019_1.miso_summary", sep="\t", index_col=None)

chr = list(df["chrom"])
start = list(df["mRNA_starts"])
end = list(df["mRNA_ends"])
name = list(df["event_name"])
score = list(len(list(df["chrom"]))*"0")
strand = list(df["strand"])

all = [("chr", chr), ("start", start), ("end", end), ("name", name), ("score", score), ("strand", strand)]

beddf = pd.DataFrame.from_items(all, index).set_index("event_name")

with open("miso_output_1.bed", "w") as file:
    file.write(pd.DataFrame.to_csv(beddf, sep="\t"))
