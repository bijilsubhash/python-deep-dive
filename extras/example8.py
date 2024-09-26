import argparse

parser = argparse.ArgumentParser(description="Prints the square of a list of numbers and cube of another list of numbers")

parser.add_argument("--sq", type=float, help="first list of numbers", nargs='*')
parser.add_argument("--cu", type=float, help="second list of numbers", nargs='+', required=True)

args = parser.parse_args()

if args.sq:
    squares = [num ** 2 for num in args.sq]
    print(squares)

cubes = [num ** 3 for num in args.cu]
print(cubes)

