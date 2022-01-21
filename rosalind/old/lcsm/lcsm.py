import sys

def parse_fasta(lines):
    seqs = []
    cur_seq = None
    for line in lines:
        if line.startswith(">"):
            if cur_seq: seqs.append(cur_seq)
            cur_seq = {
                    "id": line[1:],
                    "seq": "",
            }
        else:
            cur_seq["seq"] += line
    seqs.append(cur_seq)
    return seqs

def unique_substrs(seq, length):
    strs = []
    for i in range(len(seq) - length + 1):
        strs.append(seq[i:(i+length)])
    return list(set(strs))

def shared_motifs(seqs):
    seqs = sorted(seqs, key=len)
    ref_seq = seqs[0]
    motifs = []
    for l in range(1, len(ref_seq)+1):
        substrs = unique_substrs(ref_seq, l)
        current_motifs = unique_substrs(ref_seq, l)
        for substr in substrs:
            for seq in seqs[1:]:
                if seq.find(substr) == -1:
                    current_motifs.remove(substr)
                    break
        if len(current_motifs) > 0:
            motifs = current_motifs
        else:
            break
    return motifs

if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.readlines()]
    seqs = [s["seq"] for s in parse_fasta(lines)]
    print(shared_motifs(seqs)[0])
