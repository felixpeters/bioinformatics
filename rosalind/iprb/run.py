import sys

from iprb import calc_prob

if __name__ == "__main__":
    inputs = sys.stdin.read().strip()
    k, m, n = [int(i) for i in inputs.split(" ")]
    print(calc_prob(k, m, n))
