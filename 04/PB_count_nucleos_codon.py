nucleos = "CTACAATGTCAGTATACCCATTGCATTAGCCGGCGGCAACAGTATATT"
dictionary = {}

for i in range(0, len(nucleos), 3):
    codon = nucleos[i : i + 3]
    if len(codon) == 3:
        if codon in dictionary:
            dictionary[codon] += 1
        else:
            dictionary[codon] = 1
print(dictionary)