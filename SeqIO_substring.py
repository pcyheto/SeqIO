from Bio import SeqIO
import gzip

def substring(inputname,inputtype,number,writefilename,outputtype):
    with open(inputname,"rt") as fh, open(writefilename,"wt") as output:
        for rec in SeqIO.parse(fh,inputtype):
            rec=rec[:number]
            SeqIO.write([rec],output,outputtype)

def zipped_substring(inputname,inputtype,number,writefilename,outputtype):
    with gzip.open(inputname,"rt") as fh, open(writefilename,"wt") as output:
        for rec in SeqIO.parse(fh,inputtype):
            rec=rec[:number]
            SeqIO.write([rec],output,outputtype)


substring("FAL00432_af307028575a34db3268b4df36412691cb25b558_0.fastq","fastq",100,"output.fasta","fasta")
substring("FAL00432_af307028575a34db3268b4df36412691cb25b558_0.fastq","fastq",100,"output.fasta","fasta")
zipped_substring("FAL76452_pass_b7700786_985.fastq.gz","fastq",100,"FAL76452.fasta","fasta")
zipped_substring("FAL76452_pass_b7700786_985.fastq.gz","fastq",100,"FAL76452.fastq","fastq")


