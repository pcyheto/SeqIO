from Bio import SeqIO

n=100
with open("100.txt","w") as f:
    for record in SeqIO.parse("FAL00432_af307028575a34db3268b4df36412691cb25b558_0.fastq", "fastq"):
        f.write(">"+str(record.id)+"\n")
        f.write(str(record.seq[:n])+"\n")

with open("100fast.fastq","w") as f:
    for record in SeqIO.parse("FAL00432_af307028575a34db3268b4df36412691cb25b558_0.fastq", "fastq"):
        f.write("@"+str(record.id)+"\n")
        f.write(str(sub_rec.seq[:n])+"\n")
        f.write("+"+"\n")
        f.write(str(sub_rec.letter_annotations["phred_quality"])+"\n")

n=200
with open("200.txt","w") as f:
    for record in SeqIO.parse("FAL00432_af307028575a34db3268b4df36412691cb25b558_0.fastq", "fastq"):
        f.write(">"+str(record.id)+"\n")
        f.write(str(record.seq[:n])+"\n")


with open("200fast.fastq","w") as f:
    for record in SeqIO.parse("FAL00432_af307028575a34db3268b4df36412691cb25b558_0.fastq", "fastq"):
        f.write("@"+str(record.id)+"\n")
        f.write(str(sub_rec.seq[:n])+"\n")
        f.write("+"+"\n")
        f.write(str(sub_rec.letter_annotations["phred_quality"])+"\n")
