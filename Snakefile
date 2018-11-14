PRE = "transcripts"
GTF = "{0}.gtf.gz".format(PRE)
FASTA = "{0}.fasta.gz".format(PRE)
INDEX = "{0}.kidx".format(PRE)

rule all:
    input:
        "kallisto_out/abundance.h5"

rule index:
    input: FASTA
    output: INDEX
    shell:
        "kallisto index -i {output} {input}"

rule kallisto_quant:
    input:
        "reads_1.fastq.gz",
        "reads_2.fastq.gz",
        INDEX
    output:
        "kallisto_out",
        "kallisto_out/abundance.h5",
        "kallisto_out/abundance.tsv",
        "kallisto_out/run_info.json"
    shell:
        "kallisto quant "
        "-i {INDEX} "
        "-b 30 "
        "-o {output[0]} "
        "--genomebam --gtf {GTF} "
        "--chromosomes chrom.txt "
        "{input[0]} {input[1]}"

#rule cufflinks:
#	input 
