# Introduction to the Bioinformatics Armory
from Bio.Seq import Seq
my_seq = Seq(open('rosalind_ini.txt', 'r').read())
print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))

