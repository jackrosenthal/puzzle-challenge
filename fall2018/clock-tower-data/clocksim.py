import sys


moves = [int(x) for x in '7 2 11 18 5 10 9 8 5 3 2 2 3 5 10 4 5 1 3 10 4 2 1 5 16 8 16 18 10 6'.split()]

elevation = 0
m = 0
for c in sys.argv[1]:
    if c in ('u', 'U'):
        print(elevation)
        print('U', moves[m])
        elevation += moves[m]
        m += 1
    elif c in ('d', 'D'):
        print(elevation)
        print('D', moves[m])
        elevation -= moves[m]
        m += 1
    if elevation < 0 or elevation > 50:
        print("BROKEN")
        break
    if elevation == 50:
        print("AT TOP")
print(elevation)
