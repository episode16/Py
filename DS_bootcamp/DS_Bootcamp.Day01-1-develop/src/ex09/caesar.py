import sys

def encode(input, shift):
    res = []
    for char in input:
        if char.isalpha():
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            res.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            res.append(char)
    print(''.join(res))

def decode(input, shift):
    return encode(input, -int(shift))

if len(sys.argv) != 4:
    raise ValueError("error of args")
flag = sys.argv[1]
input = sys.argv[2]
shift = int(sys.argv[3])
if not all(ord(char) < 128 for char in input):
    raise ValueError("The script does not support your language yet")
if flag == 'encode':
    encode(input, shift)
elif flag == 'decode':
    decode(input, shift)
else:
    raise Exception("error of command")