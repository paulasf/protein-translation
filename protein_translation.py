def proteins(strand):
    proteins_list = []
    codons = get_codons(strand)

    for codon in codons:
        proteins_list.append(get_protein(str(codon)))

    return proteins_list


def get_codons(rna_code):
    begin_index = 0
    end_index = 3
    size_code = 3
    codons = []

    while end_index <= len(rna_code):
        codons.append(rna_code[begin_index:end_index])
        begin_index += size_code
        end_index += size_code
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
    return protein_dictionary[codon]
