# TP53 Comparative Sequence Analysis

This project performs a comparative sequence analysis of the TP53 gene between Human and the Toros Blind Mole Rat. The TP53 gene is a crucial tumor suppressor gene responsible for DNA repair, regulation of the cell cycle and apoptosis.

Blind mole rats are known for their remarkable cancer resistance, making them an interesting model organism for comparative genomic studies. By comparing the TP53 gene sequences, this project demonstrates basic bioinformatics analysis including sequence statistics, alignment and visualization.

---

# Pipeline

NCBI Database  
↓  
Sequence Download (FASTA)  
↓  
FASTA Quality Check  
↓  
Sequence Parsing using Python  
↓  
Sequence Length Analysis  
↓  
GC Content Calculation  
↓  
Pairwise Sequence Alignment  
↓  
Similarity Analysis  
↓  
Data Visualization  

---

# Tools

Python  
BioPython  
Matplotlib  
VSCode  
Git  
GitHub  

---

# Dataset

Sequences were obtained from the NCBI database.

Human TP53 gene sequence  
Blind Mole Rat TP53 gene sequence  

Format: FASTA

---

# Project Structure
tp53-evolution-analysis
│
├── data
│ └── raw
│ ├── human_tp53.fasta
│ └── mole_rat_tp53.fasta
│
├── scripts
│ ├── sequence_analysis.py
│ ├── alignment_analysis.py
│ └── visualization.py
│
├── results
│ ├── statistics
│ │ └── sequence_stats.txt
│ └── alignment
│ └── alignment_result.txt
│
├── docs
│ ├── sequence_length.png
│ └── gc_content.png
│
└── README.md

---

# Results

Sequence statistics including sequence length and GC content were calculated for both TP53 genes.  
Pairwise alignment was performed to evaluate sequence similarity between the species.  
Visualization scripts generated graphical comparisons of sequence length and GC content.

---

# Author

Alperen Göçmen  
Bioinformatics Student