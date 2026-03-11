from Bio import SeqIO

output = open("results/statistics/sequence_stats.txt", "w")

files = [
    "data/raw/human_tp53.fasta",
    "data/raw/mole_rat_tp53.fasta"
]

for file in files:

    for record in SeqIO.parse(file, "fasta"):

        seq = record.seq
        length = len(seq)
        gc = (seq.count("G") + seq.count("C")) / length * 100

        line = f"{record.id} | Length: {length} | GC: {round(gc,2)}%\n"

        print(line)
        output.write(line)

output.close()