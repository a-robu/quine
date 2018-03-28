
tape = <<TAPE>>
at = <<AT>>

def decode_tape(tape_part):
    return ''.join(map(chr, tape_part))

left = decode_tape(tape[:at])
middle = str(tape)
right = decode_tape(tape[at:])
print(left + middle + right)
