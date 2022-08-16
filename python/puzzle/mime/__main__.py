import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
print(n, q, file=sys.stderr)


mime_table = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_table[ext.lower()] = mt

print(mime_table, file=sys.stderr)

for i in range(q):
    fname = input()
    if '.' not in fname:
        print("UNKNOWN")
    else:
        ext = fname.lower().split('.')[-1]
        print(fname, ext, ":", file=sys.stderr)
        print(mime_table.get(ext, "UNKNOWN"))

    # mime_table = {None : "UNKNOWN"}
    # split_fname = fname.lower().split('.')
    # ext = split_fname[-1] if len(split_fname) > 1 else None
    # ...
