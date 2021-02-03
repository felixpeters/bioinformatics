import sys

def motif_locations(prots):
    return {}

if __name__ == "__main__":
    prots = [line.strip() for line in sys.stdin.readlines()]
    locs = motif_locations(prots)
    print(locs)
