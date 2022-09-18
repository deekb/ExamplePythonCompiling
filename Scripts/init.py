#! /usr/bin/python3
import configparser
from argparse import ArgumentParser
from os import path, geteuid
from platform import system
from sys import executable
# noinspection PyUnresolvedReferences
from os import _exit as quit

__license__ = "MIT"
__status__ = "Alpha"
__version__ = "1.0.0"
__author__ = "Derek Baier"
__maintainer__ = "Derek Baier"
__email__ = "derek.m.baier@gmail.com"

from Colors import Colors

hashes = {}
with open(path.join(path.dirname(__file__), "../hashes.md5")) as hash_file:
    for line in hash_file.readlines():
        hashes[line.split(":")[1].strip()] = line.split(":")[0]

APPLICATION_HASH = hashes["main.py"]

DEVELOPER = False
DEBUG = False

fg, bg = Colors.Foreground, Colors.Background

config = configparser.ConfigParser()
config.read(path.join(path.dirname(__file__), "../main.conf"))

parser = ArgumentParser(description='My Example Description (Change this in init.py)')
parser.add_argument('-v', '--version', action='store_true', help='Show version info and exit')
parser.add_argument('--debug', action='store_true', help='Enable debug output')
parser.add_argument('--developer', action='store_true', help='Enable debug and developer output')
args = parser.parse_args()


if args.version:
    print(fg.yellow + bg.green)
    print("[Program Name]: " + config["Program"]["name"])
    print("[Version]: " + config["Program"]["version"])
    print("[License]: " + config["Program"]["license"])
    print("[Author]: " + config["Program"]["author"])
    print("[Email]: " + config["Program"]["email"])

    print(Colors.reset)
    quit(0)

if "DEVELOPER" in locals() and DEVELOPER:
    print(
        fg.red + "[INIT:WARN]: Developer explicitly enforced in locals this appears to be a development server" +
        Colors.reset)
elif "developer" in args:
    DEVELOPER = args.developer


if "DEBUG" in locals() and DEBUG:
    print(
        fg.red + "[INIT:WARN]: Debug explicitly enforced in locals, this appears to be a development server" + Colors.reset)
elif "debug" in args:
    DEBUG = args.debug or DEVELOPER


EXECUTABLE = executable
ON_WINDOWS = (system() == "Windows")
IS_ROOT = (not ON_WINDOWS) and (not geteuid())

if DEBUG:
    print("[INIT:DEBUG]: Debug mode: active")
    if not DEVELOPER:
        print("[INIT:DEBUG]: Run with the --dev tag to get full developer info")

    print(f"[INIT:DEBUG]: sys.executable: {executable}")

    if DEVELOPER:
        print(f"[INIT:DEV]: __file__ {path.join(path.dirname(__file__), 'main.py')}")

if __name__ == "__main__":

    try:
        import hashlib

        with open(path.join(path.dirname(__file__), "main.py"), "rb") as f:
            file_hash = hashlib.md5()
            while chunk := f.read(8192):
                file_hash.update(chunk)
        if file_hash.hexdigest() == APPLICATION_HASH:
            if DEBUG:
                print("[INIT:DEBUG]: Main.py hash matches stored value: \"" + file_hash.hexdigest() + "\"")
            else:
                print("[INIT:INFO]: Main.py hash matches stored value")
            import main
        else:
            if DEBUG:
                print(
                    f"[INIT:DEBUG]: Main.py hash does not match stored value: \"{file_hash.hexdigest()}\" != \"{APPLICATION_HASH}\"")
            print(fg.red + "[INIT:CRITICAL]: The hash value for main.py has changed and must be updated" + Colors.reset)

    except KeyboardInterrupt:
        if DEBUG:
            print(Colors.bold + fg.red + "\r\"main\" killed by signal: KeyboardInterrupt" + Colors.reset)
        else:
            print(Colors.bold + fg.red + "\rKeyboardInterrupt" + Colors.reset)