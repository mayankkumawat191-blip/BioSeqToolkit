# BioSeq Toolkit

## Overview

BioSeq Toolkit is a Python-based command-line tool designed for basic bioinformatics analysis of DNA sequences in FASTA format.

This project was built as a learning exercise to understand how computational biology tools process genomic data and perform sequence-level analysis.

It simulates core operations commonly used in bioinformatics workflows such as GC content calculation, reverse complement generation, and protein translation.

---

## Objectives of the Project

The main objectives of this project are:

- To understand the FASTA file format and its role in bioinformatics
- To implement DNA sequence parsing using Python
- To perform basic genomic analysis operations
- To simulate real-world bioinformatics pipeline steps
- To strengthen Python and Linux command-line skills

---

## Features

The toolkit provides the following functionalities:

### 1. FASTA File Parsing
- Reads DNA sequences from FASTA formatted files
- Supports multiple sequences in a single file

### 2. GC Content Calculation
- Computes percentage of Guanine (G) and Cytosine (C)
- Helps analyze DNA stability and composition

### 3. Reverse Complement Generation
- Generates complementary DNA strand
- Useful in DNA strand analysis

### 4. DNA to Protein Translation
- Converts DNA sequence into amino acid sequence
- Uses standard codon mapping

### 5. Motif Search
- Identifies specific nucleotide patterns in DNA sequences
- Returns positions where motif is found

---

## Technologies Used

- Python 3
- Linux Terminal
- Git & GitHub

---

## Project Structure

```text
BioSeqToolkit/
│
├── bioseq_toolkit.py   # Main Python script
├── sample.fasta        # Example DNA input file
├── README.md           # Project documentation
