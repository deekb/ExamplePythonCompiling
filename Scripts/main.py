# Import the tool for getting the real path to a file relative to this script (works when debugging and when compiled)
from tools import AbsolutePath

# Alias AbsolutePath to make it quicker to type
path = AbsolutePath

print(f"hello from {path('main.py')}")