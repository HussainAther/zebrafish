chr_range = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "M"]

o = open("/data/athersh/Danio_rerio.GRCz11.95.fixed.gff3", "w") 

with open("/data/athersh/Danio_rerio.GRCz11.95.gff3", "r") as file:
    for line in file:
        if line.split("\t")[0] in chr_range:
            o.write("chr" + str(line))
