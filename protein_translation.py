def proteins(strand):
    proteins_list = []
    codons = extract_codons(strand)
    protein = ''

    try:
        for codon in codons:
            protein = get_protein(codon)
            if protein == "STOP":
                break
            proteins_list.append(protein)    
    except KeyError:
        print('Invalid key')
    return proteins_list


def extract_codons(rna_code):
    size = 3
    codons = [rna_code[i:i + size] for i in range(0, len(rna_code), size)]
    return codons


def get_protein(codon):
    protein_dictionary = {
      'AUG': "Methionine",
      'UGG': "Tryptophan",
      'UUC': "Phenylalanine",
      'UUU': "Phenylalanine",
      'UUA': "Leucine",
      'UUG': "Leucine",
      'UCU': "Serine",
      'UCC': "Serine",
      'UCA': "Serine",
      'UCG': "Serine",
      'UAU': "Tyrosine",
      'UAC': "Tyrosine",
      'UGU': "Cysteine",
      'UGC': "Cysteine",
      'UAG': "STOP",
      'UGA': "STOP"
    }

    if codon not in protein_dictionary:
        raise KeyError("Unknown key!")

    return protein_dictionary[codon]
