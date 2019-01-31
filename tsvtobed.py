import pandas as pd

df = pd.DataFrame.from_csv("summary_miso_output_2019_1/summary/miso_output_2019_1.miso_summary", sep="\t", index_col=False)

chr = list(df["chrom"])
start = list(df["mRNA_starts"])
end = list(df["mRNA_ends"])
name = list(df["event_name"])
score = list(len(df["chrom"])*"\t")
strand = list(df["strand"])

all = [chr, start, end, name, score, strand]
labels = ["chr", "start", "end", "name", "score", "strand"]

beddf = pd.DataFrame.from_records(all, columns=labels)

with open("miso_output_1.bed", "w") as file:
    file.write(pd.DataFrame.to_csv(beddf, sep="\t"))
