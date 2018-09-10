import sys
import argparse
import string

# This was mostly a copy-paste of an older program I had written ~2015.
# The puzzle only uses Rotor #5

rotors = {
        1: list(string.ascii_uppercase),
        2: ['Q', 'R', 'X', 'I', 'S', 'L', 'M', 'Y', 'T', 'P', 'C', 'A', 'Z', 'U', 'F', 'V', 'N', 'K', 'O', 'W', 'E', 'G', 'B', 'D', 'H', 'J'],
        3: ['M', 'I', 'S', 'T', 'Y', 'C', 'F', 'R', 'N', 'B', 'L', 'Z', 'G', 'D', 'P', 'E', 'Q', 'H', 'O', 'W', 'A', 'V', 'K', 'X', 'J', 'U'],
        4: ['X', 'B', 'Q', 'I', 'J', 'T', 'P', 'U', 'Y', 'R', 'F', 'C', 'Z', 'D', 'A', 'S', 'V', 'L', 'W', 'M', 'O', 'K', 'G', 'H', 'N', 'E'],
        5: ['K', 'X', 'W', 'M', 'T', 'P', 'A', 'V', 'I', 'N', 'F', 'Y', 'E', 'C', 'R', 'Q', 'Z', 'U', 'L', 'D', 'G', 'J', 'O', 'S', 'B', 'H'],
        6: ['R', 'C', 'S', 'O', 'K', 'M', 'X', 'J', 'Z', 'A', 'P', 'H', 'L', 'I', 'B', 'D', 'F', 'V', 'N', 'G', 'Q', 'T', 'E', 'W', 'Y', 'U']
}

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decrypt",
    action="store_true",
    help="Decrypt a message")
parser.add_argument("-r", "--rotor",
    type=int,
    default=5,
    help="Rotor number to select (5 is default)")
parser.add_argument("-a", "--amount",
    type=int,
    default=1,
    help="Amount to rotate each time")
parser.add_argument("-f", "--freq",
    type=int,
    default=1,
    help="Frequency to rotate")
parser.add_argument("-k", "--ref",
    type=str,
    default='A',
    help="Reference letter to start at")
parser.add_argument("-m", "--message",
    type=argparse.FileType('r'),
    default=sys.stdin,
    help="File to read message from (defaults to stdin)")
args = parser.parse_args()

rotor = rotors[args.rotor]

def rturn(amount=1):
    if amount >= 1:
        for i in range(amount):
            rotor.append(rotor.pop(0))
    if amount <= -1:
        for i in range(-1*amount):
            rotor.insert(0, rotor.pop())

def ref_set(letter):
    if letter not in rotor:
        raise ValueError
    while rotor[25] != letter:
        rturn()

ref_set(args.ref.upper())

freq_at = 0
def freqinc():
    global freq_at
    freq_at += 1
    if freq_at == args.freq:
        rturn(args.amount)
        freq_at = 0

if not args.decrypt:
    def code(letter):
        let = rotor[string.ascii_uppercase[::-1].find(letter)]
        freqinc()
        return let
else:
    def code(letter):
        let = string.ascii_uppercase[::-1][rotor.index(letter)]
        freqinc()
        return let

for letter in args.message.read().upper():
    if letter in string.ascii_uppercase:
        print(code(letter), end="")
    else:
        print(letter, end="")
