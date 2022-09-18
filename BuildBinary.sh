#!/bin/bash
export PROGNAME="Example Python Compiling"
nuitka3 --onefile --standalone --include-data-file=./hashes.md5=./default.conf --include-data-file=./main.conf=./main.conf --include-data-file=./Scripts/main.py=./Scripts/main.py --include-data-file=./README.md=./README.md --output-dir=/tmp/nuitka/ --remove-output -o "./Generated-Binaries/$PROGNAME" ./Scripts/init.py