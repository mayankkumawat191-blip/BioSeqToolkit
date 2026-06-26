import argparse


def read_fasta(file):
    sequences = {}
    header = None

    with open(file, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                header = line[1:].strip()
                sequences[header] = ""
            else:
                if header is None:
                    continue
                sequences[header] += line.upper()

    return sequences


def gc_content(seq):
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")

    if len(seq) == 0:
        return 0

    return round((gc / len(seq)) * 100, 2)


def reverse_complement(seq):
    comp = {"A":"T","T":"A","G":"C","C":"G"}
    return "".join(comp.get(base, "N") for base in reversed(seq.upper()))


def translate_dna(seq):
    codon_table = {
        "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
        "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
        "ATT":"I","ATC":"I","ATA":"M","ATG":"M",
        "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
        "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
        "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
        "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
        "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
        "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
        "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
        "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
        "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
        "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
        "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
        "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
        "GGT":"G","GGC":"G","GGA":"G","GGG":"G"
    }

    seq = seq.upper()
    protein = ""

    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, "X")

    return protein


def find_motif(seq, motif):
    seq = seq.upper()
    motif = motif.upper()

    positions = []

    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i+len(motif)] == motif:
            positions.append(i + 1)

    return positions


# ---------------- CLI ----------------

parser = argparse.ArgumentParser(description="BioSeq Toolkit Final Version")

parser.add_argument("file", help="FASTA file")

parser.add_argument("--gc", action="store_true", help="GC content")
parser.add_argument("--revcomp", action="store_true", help="Reverse complement")
parser.add_argument("--translate", action="store_true", help="DNA to protein")
parser.add_argument("--motif", help="Motif search")

args = parser.parse_args()

sequences = read_fasta(args.file)


for name, seq in sequences.items():

    if args.gc:
        print(f"{name} -> GC Content: {gc_content(seq)} %")

    if args.revcomp:
        print(f"{name} -> Reverse Complement:")
        print(reverse_complement(seq))

    if args.translate:
        print(f"{name} -> Protein Sequence:")
        print(translate_dna(seq))

    if args.motif:
        positions = find_motif(seq, args.motif)

        if positions:
            print(f"{name} -> Motif '{args.motif}' found at: {positions}")
        else:
            print(f"{name} -> Motif '{args.motif}' not found")
