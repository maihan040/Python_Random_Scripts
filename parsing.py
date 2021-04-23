import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here")
#parser.add_argument("square", help="display a spare of a given number", type=int)
parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
