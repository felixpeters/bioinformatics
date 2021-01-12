import operator

def dna_dict(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    dna_dict = {}
    current_key = ""
    for line in lines:
        if line.startswith(">"):
            current_key = line[1:]
            dna_dict[current_key] = ""
        else:
            dna_dict[current_key] += line
    return dna_dict

def calc_gc(seq):
    return (seq.count("C") + seq.count("G")) / len(seq) * 100

def gc_dict(dna_dict):
    gc_dict = {sid: calc_gc(seq) for sid, seq in dna_dict.items()}
    return gc_dict

def max_gc(gc_dict):
    return max(gc_dict.items(), key=operator.itemgetter(1))

def max_gc_seq(file):
    dd = dna_dict(file)
    gd = gc_dict(dd)
    return max_gc(gd)

