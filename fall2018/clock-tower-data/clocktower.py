import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--height',
    type=int,
    default=50,
    help='Tower height')
parser.add_argument(
    'moves',
    nargs='+',
    type=int,
    help='Moves in order')
args = parser.parse_args()


height = args.height
moves = args.moves


def dfs(h=0, idx=0, seen_top=False):
    global height
    global moves
    if h == height:
        seen_top = True
    elif h == 0 and seen_top:
        yield ''
        return
    rem = sum(moves[idx:])
    if h - rem > 0:
        return
    if not seen_top and h + rem < height:
        return
    upmove = h + moves[idx]
    downmove = h - moves[idx]
    if upmove <= height:
        for nxt in dfs(h=upmove, idx=idx + 1, seen_top=seen_top):
            yield 'U' + nxt
    if downmove >= 0:
        for nxt in dfs(h=downmove, idx=idx + 1, seen_top=seen_top):
            yield 'D' + nxt


for seq in dfs():
    print(seq)
