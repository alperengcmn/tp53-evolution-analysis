from Bio import SeqIO
from Bio import pairwise2

human = SeqIO.read("data/raw/human_tp53.fasta", "fasta")
mole = SeqIO.read("data/raw/mole_rat_tp53.fasta", "fasta")

seq1 = human.seq
seq2 = mole.seq

alignments = pairwise2.align.globalxx(seq1, seq2)

best_alignment = alignments[0]

score = best_alignment.score
length = max(len(seq1), len(seq2))

similarity = (score / length) * 100

output = open("results/alignment/alignment_result.txt","w")

output.write(f"Alignment score: {score}\n")
output.write(f"Sequence similarity: {round(similarity,2)}%\n")

print("Alignment score:", score)
print("Sequence similarity:", round(similarity,2), "%")

output.close()