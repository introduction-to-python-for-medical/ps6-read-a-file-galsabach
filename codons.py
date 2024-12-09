def create_codon_dict(file_path):
  file_path = "data/codons.txt"
  file = open(file_path)
  rows = file.readlines()
  file.close()

  dic = {}
  for row in rows:
    row = row.strip().split('\t')
    codon = row[0]
    amino_acid = row[2]
    dic[codon] = amino_acid
  return dic

