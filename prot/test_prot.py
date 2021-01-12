from prot import translate_rna

def test_translate_rna():
    rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    protein = "MAMAPRTEINSTRING"
    assert translate_rna(rna) == protein
