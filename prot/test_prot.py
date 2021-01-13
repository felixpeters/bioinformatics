from prot import translate_rna, translate_rna_bp

def test_translate_rna():
    rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    protein = "MAMAPRTEINSTRING"
    assert translate_rna(rna) == protein

def test_translate_rna_bp():
    rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    protein = "MAMAPRTEINSTRING"
    assert str(translate_rna_bp(rna)) == protein


