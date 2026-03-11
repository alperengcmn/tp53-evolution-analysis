import matplotlib.pyplot as plt
from Bio import SeqIO

files = [
    "data/raw/human_tp53.fasta",
    "data/raw/mole_rat_tp53.fasta"
]

names = []
lengths = []
gc_values = []

for file in files:

    for record in SeqIO.parse(file, "fasta"):

        seq = record.seq

        length = len(seq)
        gc = (seq.count("G") + seq.count("C")) / length * 100

        names.append(record.id)
        lengths.append(length)
        gc_values.append(gc)

plt.figure()

plt.bar(names, lengths)
plt.title("TP53 Sequence Length Comparison")
plt.ylabel("Base Pairs")

plt.savefig("docs/sequence_length.png")

plt.figure()

plt.bar(names, gc_values)
plt.title("TP53 GC Content Comparison")
plt.ylabel("GC %")

plt.savefig("docs/gc_content.png")