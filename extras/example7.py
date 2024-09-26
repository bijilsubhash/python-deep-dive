import argparse
import datetime

parser = argparse.ArgumentParser(description="Returns a string containing the name and age of the person")

parser.add_argument("-f", "--first", type=str, help="first name of the person", required=False, dest="first_name")
parser.add_argument("-l", "--last", type=str, help="last name of the person", required=True, dest="last_name")
parser.add_argument("--yob", type=int, help="year of birth of the person", required=False, dest='birth_year')

args = parser.parse_args()

if args.first_name:
    names = [args.first_name]
else:
    names = []

names.append(args.last_name)
full_name = " ".join(names)

current_year = datetime.datetime.now().year
age = current_year - args.birth_year

print(f"Hello {full_name}, you are {age} years old")

