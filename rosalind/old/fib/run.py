import sys

from fib import pairs

if __name__ == "__main__":
    inputs = sys.stdin.read().strip()
    n, k = [int(i) for i in inputs.split(" ")]
    print(pairs(n, k))
