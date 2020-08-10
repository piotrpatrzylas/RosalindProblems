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

# Data Formats

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "piotrpatrzylas@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["JX914595 NM_001266228 JQ011270 NM_001194889 JX308815 NM_001015511 JX428803 NM_001082732"], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))
lowest = 0
for i in range(len(records)-1):
    if len(records[i+1].seq) < len(records[lowest]):
        lowest = i
handle2 = Entrez.efetch(db="nucleotide", id=[records[lowest].id], rettype="fasta")
records = handle2.read()
print (records)