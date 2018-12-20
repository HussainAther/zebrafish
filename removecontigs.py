
with open("/data/athersh/slurm-15867947.out", "r") as file:
	for line in file.readlines():
		if "reference contigs" in line:
			error_contigs=[ line.replace(" reference contigs = [", "").replace(" ","").replace("]", "").replace("\n", "").split(",")] 

with open("/data/athersh/errorcontigs.txt", "a") as file:
	for item in error_contigs:
		for subitem in item:
			file.write(subitem)
			file.write("\n")
