#! /bin/bash
# gatk.bat
set -e

module load GATK/3.5-0 || exit 1

cd /data/athersh/

# use 8 GB memory
java -Xmx8g -Djava.io.tmpdir=/lscratch/$SLURM_JOBID -jar $GATK_JAR \
	-T CountReads \
	-R Danio_rerio.GRCz10.cdna.all.fa \
	-I 2016/R1/Aligned.out.sorted.bam \
	-et NO_ET -K $GATK_KEY
