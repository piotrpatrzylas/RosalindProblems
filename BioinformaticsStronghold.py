# Counting DNA Nucleotides
s = input()
print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))

# Transcribing DNA into RNA
s = input()
print(s.replace("T", "U"))

# Complementing a Strand of DNA
s = input()
s = s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print(s)

# Counting Point Mutations
s1 = input()
s2 = input()
hamming_dist = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        hamming_dist += 1

# Translating RNA into Protein
s = input()
codon_diki = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
              "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
              "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
              "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
              "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
              "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
              "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
              "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
              "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
              "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
              "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
              "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
              "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
              "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
              "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
              "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
results = ""
codons = int(len(s)/3)
for i in range(codons-1):
    results += codon_diki[str(s[0:3])]
    s = s[3:]
print(results)

# Finding a Motif in DNA
s1 = input()
s2 = input()
lens2 = len(s2)
results = []
for i in range(len(s1)-lens2+1):
    if (s1[i:i+lens2]) == s2:
        results += [str(i+1)]
print(*results)

# Computing GC Content
file = open("/home/piotr/Desktop/ros.txt", "r")
text = file.read().splitlines()
dna_no = 0
indices = []
for i in range(len(text)):
    if ">" in text[i]:
        dna_no += 1
        indices += [i]
diki = {}


def cg(s):
    occur = 0
    for letter in s:
        if letter == "C" or letter == "G":
            occur += 1
    return round((occur / len(s) * 100), 10)


for i in range(dna_no):
    if i == list(range(dna_no))[-1]:
        diki[text[indices[i]]] = ["". join(text[indices[i]+1:])]
        diki[text[indices[i]]] = diki[text[indices[i]]][0]
    else:
        diki[text[indices[i]]] = ["". join(text[indices[i]+1:indices[i+1]])]
        diki[text[indices[i]]] = diki[text[indices[i]]][0]
CG_content = 0
label = ""
for key, value in diki.items():
    if cg(value) > CG_content:
        CG_content = cg(value)
        label = key
        label = label.replace(">", "")
print(label, "\n", CG_content)

# Rabbits and Recurrence Relations

# Locating Restriction Sites
with open ("rosalind_revp.txt","r") as file:
    seq = ''.join(file.read().splitlines()[1:])


def palindrome(string):
    string = string.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
    return string


def get_seq(string, size):
    for i in range(len(s)-(size-1)):
        if s[i:i+size] == palindrome(s[i:i+size])[::-1]:
            print(i+1, size)


def locate_rs(string, lbound, ubound):
    for i in range(lbound,ubound):
        get_seq(string, i)


locate_rs(seq, 4, 13)

# Calculating Protein Mass

mmt = {"A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
       "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
       "K": 128.09496, "L":  113.08406, "M": 131.04049, "N": 114.04293,
       "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
       "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}

protein = "PRQTEINSTRING"
pmass = 0
for i in protein:
    pmass += mmt[i]
print(pmass)

# Mendel's First Law

AA = 30
Aa = 17
aa = 23
ts = AA + Aa + aa
probability = ((AA*(AA-1)) + (AA*Aa*2) + (AA*aa*2) + ((Aa * (Aa-1))*0.75) + (Aa*aa)) / ts / (ts-1)
print(probability)

# RNA Splicing

file = open("/home/piotr/Desktop/rosalind_splc.txt", "r")
raw_data = file.read().splitlines()
DNA_full = raw_data[1]
for i in range(2, len(raw_data)):
    if i % 2 == 0:
        continue
    else:
        DNA_full = DNA_full.replace(raw_data[i], "")
RNA_removed = DNA_full.replace("T", "U")
protein = ""
for i in range((len(RNA_removed)//3)-1):
    protein += codon_diki[RNA_removed[:3]]
    RNA_removed = RNA_removed[3:]
print(protein)