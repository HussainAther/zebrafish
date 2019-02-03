#!/bin/bash
#SBATCH --job-name="misc"
#SBATCH --partition="norm"
#SBATCH --time=72:00:00

#interpret arguments
GZIPSCRIPT=$1
if [ -z $2 ]; then
    EXTRA=$2
else
     EXTRA=''
fi

gzip Undetermined_S0_L001_R1_001.fastq
gzip Undetermined_S0_L002_R1_001.fastq
gzip Undetermined_S0_L001_R2_001.fastq
gzip Undetermined_S0_L002_R2_001.fastq

$PID = $!

finish(){
    echo 'Finished gzip.'
    kill -SIGINT $SNAKE_PID
    exit 0
}
trap finish SIGTERM

wait $PID
