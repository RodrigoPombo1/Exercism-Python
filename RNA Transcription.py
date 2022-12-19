def to_rna(dna_strand):
    adict = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    result = ""
    for char in dna_strand:
        result += adict[char]
    return result
