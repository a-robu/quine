import sys

fn = 'quine.py'

if len(sys.argv) >= 2:
    fn = sys.argv[1]

with open(fn) as f:
    raw_contents = f.read()
    left, raw_right = raw_contents.split('<<TAPE>>')
    at = len(left)
    right = raw_right.replace('<<AT>>', str(at))
    middle = str(list(map(ord, left + right)))
    print(left + middle + right)
