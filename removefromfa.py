
error_contigs = []
with open("/data/athersh/errorcontigs.txt", "r") as file:
	for line in file:
		error_contigs.append(line.replace("\n", ""))

error = 0

new = open("/data/athersh/Danio_rerio.GRCz10.cdna.all.fa.corrected", "a") 

error_dict_output = open("/data/athersh/error_dict.txt")
error_dict = {}

with open("/data/athersh/Danio_rerio.GRCz10.cdna.all.fa", "r") as file:
	if line.startswith(">"):
		contig = line.split(" ")[0].replace(">", "")
		chr = line.split(":")[1]
		start = line.split(":")[2]
		end = line.split(":")[3]
		strand = line.split(":")[4]
		if line.split(" ")[0].replace(">", "") in error_contigs:
			error = 1
			error_dict[contig] = chr + ":" start + ":" + end + ":" + strand 
		elif line[0] == ">":
			error = 0
#	if error == 0:
#		new.write(line)
#		new.write("\n")

