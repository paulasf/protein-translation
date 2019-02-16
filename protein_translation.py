def proteins(strand):
    proteins_list = []
    codons = extract_codons(strand)
    protein = ''

    try:
        for codon in codons:
            protein = get_protein(str(codon))
            if protein != "STOP":
                proteins_list.append(protein)
            else:
                return proteins_list
    except KeyError:
        return proteins_list
    return proteins_list


def extract_codons(rna_code):
    index = 0
    size_codon = 3
    codons = []

    while index + size_codon <= len(rna_code):
        codons.append(rna_code[index:index + size_codon])
        index += size_codon
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
