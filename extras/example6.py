import argparse

parser = argparse.ArgumentParser(description="Calculates the div a // b and mod a % b of two integers")

parser.add_argument("a", type=int, help="first integer")
parser.add_argument("b", type=int, help="second integer")

args = parser.parse_args()
a = args.a
b = args.b

print(a // b, a % b)
