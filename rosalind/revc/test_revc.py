from revc import revc

def test_revc():
    dna = "AAAACCCGGT"
    assert revc(dna) == "ACCGGGTTTT"
