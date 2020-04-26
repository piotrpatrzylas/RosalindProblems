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
