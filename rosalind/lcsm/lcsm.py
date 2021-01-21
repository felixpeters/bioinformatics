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

def shared_motifs(seqs):
    return []

if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.readlines()]
    seqs = [s["seq"] for s in parse_fasta(lines)]
    print(shared_motifs(seqs))
