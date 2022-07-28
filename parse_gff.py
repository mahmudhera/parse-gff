import argparse
from Bio import SeqIO

def parse_args():
    p = argparse.ArgumentParser(description="Parses a GFF file, and then list all coding genes")
    p.add_argument("fname", help="name of the GFF file")
    #p.add_argument("--scaled", help="scaling factor of the sketch", default=0.1)
    #p.add_argument("-k", "--ksize", type=int, default=21, help="kmer size")
    #p.add_argument("-s", "--seed", type=int, help="random seed for simulations")
    args = p.parse_args()
    return args

def read_features(fname):
    f = open(fname)
    lines = f.readlines()
    lines_ = [l.strip().split('\t') for l in lines if l[0] != '#']
    return lines_

args = parse_args()
print(args.fname)
lines = read_features(args.fname)
genes = [l for l in lines if l[2] == 'CDS']
for i in range(1):
    print(genes[i])
    print('')

print( len(genes) )

fasta_filename = 'GCF_001989575.1_ASM198957v1_genomic.fna'
for record in SeqIO.parse(fasta_filename, "fasta"):
    if record.id == genes[0][0]:
        start = int(genes[0][3])
        end = int(genes[0][4])
        print(record.seq[start:end])
