#!/bin/python3
from argparse import ArgumentParser
from os import path, name, geteuid

parser = ArgumentParser(description='My Example Description (Change this in init.py)')
parser.add_argument('--debug', action='store_true', help='Enable debug output')
args = parser.parse_args()

INSTALLED = (path.dirname(path.abspath(__file__)) == path.join(path.sep, "usr", "bin"))
ON_WINDOWS = (name == "nt")
IS_ROOT = (not geteuid())
DEBUG = args.debug

if DEBUG:
    print("Debug mode is active")
    print(f"INSTALLED?: {INSTALLED}")
    print(f"ON_WINDOWS?: {ON_WINDOWS}")
    print("you are seeing this message because you ran this script with the --debug flag")

if __name__ == "__main__":
    try:
        import main
    except KeyboardInterrupt:
        print()
        print("KeyboardInterrupt")
