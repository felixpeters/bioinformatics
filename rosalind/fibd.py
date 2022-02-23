import sys

from bioinformatics.heredity import mortal_fibonacci

if __name__ == "__main__":
    inputs = sys.stdin.read().strip()
    periods, lifespan = [int(i) for i in inputs.split(" ")]
    print(mortal_fibonacci(periods, lifespan))
