from argparse import ArgumentParser
import hashlib
import os

parser = ArgumentParser()
parser.add_argument('--ReHash', action='store_true', help='Generate new hashes for libraries')
args = parser.parse_args()

if args.ReHash:
    with open("hashes.md5", "w") as hashfile:
        for _file in os.listdir("./"):
            if _file.endswith(".py"):
                with open(_file, "rb") as f:
                    file_hash = hashlib.md5()
                    while chunk := f.read(8192):
                        file_hash.update(chunk)
                hashfile.write(file_hash.hexdigest() + ":" + _file + "\n")
                print(f"ReHashed {_file}")
        
