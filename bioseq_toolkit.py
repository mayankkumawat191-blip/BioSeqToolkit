
import argparse

def read_fasta(file):
    sequence = ""
    with open(file, "r") as f:
        for line in f:
            if not line.startswith(">"):
                sequence += line.strip().upper()
    return sequence

def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return round((gc / len(seq)) * 100, 2)

def reverse_complement(seq):
    comp = {"A":"T", "T":"A", "G":"C", "C":"G"}
    return "".join(comp.get(base, base) for base in reversed(seq))

def translate_dna(seq):
    codon_table = {
        "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
        "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
        "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
        "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
        "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
        "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
        "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",
        "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
    }
    protein = ""
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, "X")
    return protein

parser = argparse.ArgumentParser(description="BioSeq Toolkit")
parser.add_argument("file", help="FASTA file")
parser.add_argument("--gc", action="store_true", help="Calculate GC content")
parser.add_argument("--revcomp", action="store_true", help="Reverse complement")
parser.add_argument("--translate", action="store_true", help="Translate DNA to protein")

args = parser.parse_args()
seq = read_fasta(args.file)

if args.gc:
    print(f"GC Content: {gc_content(seq)}%")

if args.revcomp:
    print("Reverse Complement:")
    print(reverse_complement(seq))

if args.translate:
    print("Protein Sequence:")
    print(translate_dna(seq))

