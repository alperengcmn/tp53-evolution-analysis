from Bio import SeqIO

for record in SeqIO.parse("data/raw/human_tp53.fasta", "fasta"):
    print("ID:", record.id)
    print("Length:", len(record.seq))