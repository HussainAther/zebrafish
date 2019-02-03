#!/bin/bash
#SBATCH --job-name="misc"
#SBATCH --partition="norm"
#SBATCH --cpus-per-task=24
#SBATCH --mem=24g
#SBATCH --time=72:00:00

gzip Undetermined_S0_L001_R1_001.fastq
gzip Undetermined_S0_L002_R1_001.fastq
gzip Undetermined_S0_L001_R2_001.fastq
gzip Undetermined_S0_L002_R2_001.fastq

$PID = $!

finish(){
    echo 'Finished gzip.'
    kill -SIGINT $PID
    exit 0
}
trap finish SIGTERM

wait $PID
