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
    comp = {"A":"T","T":"A","G":"C","C":"G"}
    return "".join(comp.get(base, base) for base in reversed(seq))

parser = argparse.ArgumentParser(description="BioSeq Toolkit")
parser.add_argument("file", help="FASTA file")
parser.add_argument("--gc", action="store_true", help="Calculate GC content")
parser.add_argument("--revcomp", action="store_true", help="Reverse complement")

args = parser.parse_args()

seq = read_fasta(args.file)

if args.gc:
    print("GC Content:", gc_content(seq), "%")

if args.revcomp:
    print("Reverse Complement:")
    print(reverse_complement(seq))

