import argparse

parser = argparse.ArgumentParser(description="mutually exclusive arguments")

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true')
group.add_argument('-q', '--quiet', action='store_true')

parser.add_argument('x', type=int, help='the base')

args = parser.parse_args()

print(args)

if args.quiet:
    print('quiet mode...')
    print('nothing to see here...')

if args.verbose:
    print('verbose mode...')
    print('this is the base:', args.x)

