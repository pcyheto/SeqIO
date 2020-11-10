from Bio import SeqIO
import gzip

n=100
with gzip.open("FAL76452_pass_b7700786_985.fastq.gz","rt") as source:
    with open("100fast.fastq","w") as f:
        for record in SeqIO.parse(source, "fastq"):
            sub_rec=record[:n]
            f.write("@"+str(record.id)+"\n")
            f.write(str(sub_rec.seq[:n])+"\n")
            f.write("+"+"\n")
            f.write(str(sub_rec.letter_annotations["phred_quality"])+"\n")

with gzip.open("FAL76452_pass_b7700786_985.fastq.gz","rt") as source:
    with open("100.txt","w") as f:
        for record in SeqIO.parse(source, "fastq"):
            f.write(">"+str(record.id)+"\n")
            f.write(str(record.seq[:n])+"\n")

n=200
with gzip.open("FAL76452_pass_b7700786_985.fastq.gz","rt") as source:
    with open("200.txt","w") as f:
        for record in SeqIO.parse(source, "fastq"):
            f.write(">"+str(record.id)+"\n")
            f.write(str(record.seq[:n])+"\n")

with gzip.open("FAL76452_pass_b7700786_985.fastq.gz","rt") as source:
    with open("200fast.fastq","w") as f:
        for record in SeqIO.parse(source, "fastq"):
            sub_rec=record[:n]
            f.write("@"+str(record.id)+"\n")
            f.write(str(sub_rec.seq[:n])+"\n")
            f.write("+"+"\n")
            f.write(str(sub_rec.letter_annotations["phred_quality"])+"\n")
