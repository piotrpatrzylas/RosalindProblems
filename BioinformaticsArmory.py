# Introduction to the Bioinformatics Armory
from Bio.Seq import Seq
my_seq = Seq(open('rosalind_ini.txt', 'r').read())
print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))

# GenBank Introduction
from Bio import Entrez
Entrez.email = "piotrpatrzylas@gmail.com"
handle = Entrez.esearch(db="nucleotide", term='"Ananas"[Organism] AND "2006/01/05"[PDAT] : "2010/08/17"[PDAT]')
record = Entrez.read(handle)
print(record["Count"])
