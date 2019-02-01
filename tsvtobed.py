import pandas as pd

def create_bed(input, output):
    df = pd.DataFrame.from_csv(input, sep="\t", index_col=None)

    chr = list(df["chrom"])
    start = list(df["mRNA_starts"])
    end = list(df["mRNA_ends"])
    name = list(df["event_name"])
    score = list(len(list(df["chrom"]))*"0")
    strand = list(df["strand"])

    all = [("chr", chr), ("start", start), ("end", end), ("name", name), ("score", score), ("strand", strand)]

    beddf = pd.DataFrame.from_items(all).set_index("chr")

    with open(output, "w") as file:
        file.write(pd.DataFrame.to_csv(beddf, sep="\t"))
    return

input_output = {"summary_miso_output_2019_1/summary/miso_output_2019_1.miso_summary":"miso_output_2019_1.bed",
        "summary_miso_output_2019_7/summary/miso_output_2019_7.miso_summary":"miso_output_2019_7.bed",
        "summary_miso_output_2019_1control/summary/miso_output_2019_1control.miso_summary":"miso_output_2019_1control.bed",
        "summary_miso_output_2019_7control/summary/miso_output_2019_7control.miso_summary":"miso_output_2019_7control.bed"}

for i in input_output:
    create_bed(i, input_output[i])
