#!/bin/bash
nuitka3 --onefile --standalone ./init.py --include-data-file=./hashes.md5=./default.conf --include-data-file=./main.conf=./main.conf --include-data-file=./main.py=./main.py --include-data-file=./README.md=./README.md --include-data-file=./hashes.md5=./hashes.md5 -o ./init