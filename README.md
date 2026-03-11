# TP53 Comparative Sequence Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Bioinformatics](https://img.shields.io/badge/Field-Bioinformatics-green)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

This project performs a comparative sequence analysis of the TP53 gene between Human and the Toros Blind Mole Rat.

The TP53 gene is a critical tumor suppressor gene involved in DNA repair, cell cycle regulation and apoptosis. Blind mole rats are known for their remarkable cancer resistance, making them a valuable model organism for comparative genomic studies.

The aim of this project is to demonstrate a simple bioinformatics pipeline including sequence statistics, alignment and visualization using Python.

---

# Bioinformatics Pipeline

NCBI Database  
↓  
Sequence Download (FASTA)  
↓  
FASTA Quality Control  
↓  
Sequence Parsing with Python  
↓  
Sequence Length Analysis  
↓  
GC Content Calculation  
↓  
Pairwise Sequence Alignment  
↓  
Similarity Calculation  
↓  
Data Visualization  

---

# Tools and Technologies

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

## Project Structure

```
tp53-evolution-analysis
│
├── data
│   └── raw
│       ├── human_tp53.fasta
│       └── mole_rat_tp53.fasta
│
├── scripts
│   ├── sequence_analysis.py
│   ├── alignment_analysis.py
│   └── visualization.py
│
├── results
│   ├── statistics
│   │   └── sequence_stats.txt
│   │
│   └── alignment
│       └── alignment_result.txt
│
├── docs
│   ├── sequence_length.png
│   └── gc_content.png
│
└── README.md
```

---

# Results

Sequence statistics including sequence length and GC content were calculated for both TP53 genes.

Pairwise alignment was performed to estimate sequence similarity between the two species.

Visualization scripts generated graphical comparisons of sequence length and GC content.

---

# Author

Alperen Göçmen  
Bioinformatics Student