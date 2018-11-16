# Used to locate and analyze the SNPs in RNA-Seq data

samples = {"Undetermined_S0_L001_R1_001.fasta":"snp/L001_R1_report", 
   		  "Undetermined_S0_L002_R1_001.fasta":"snp/L002_R1_report", 
		  "Undetermined_S0_L001_R2_001.fasta":"snp/L001_R2_report",
		  "Undetermined_S0_L002_R2_001.fasta":"snp/L002L_R2_report"}

ref = "Danio_rerio.GRCz10.cdna.all.fa"

for sample in samples
	f = open(str(sample), "r")
	o = open(str(samples[sample]), "a")
	count = 0
	for line in f.readlines():
		if line[0] != ">":
			sampleline = line
		for line in 
			count += 1

