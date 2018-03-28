import sys

fn = sys.argv[1]

with open(fn) as f:
    raw_contents = f.read()
    left, raw_right = raw_contents.split('<<TAPE>>')
    # `at` is the index where the tape begins.
    at = len(left)
    right = raw_right.replace('<<AT>>', str(at))
    middle = str([ord(x) for x in left + right])
    print(left + middle + right)
