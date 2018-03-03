from random import randint
import sys

# g, d, f = list(map(int, input().split(' ')))
g, d, f = list(map(int, sys.argv[1:]))
mx = g + d + f - 1
used = set()
def gen_arr(ln, used):
    arr = []
    # for i in range(ln):
    i = 0
    while i < ln:
        val = randint(1, mx + 1)
        if val not in used:
            arr.append(str(val))
            used.add(val)
            i += 1
    return [arr, used]

g_arr, used = gen_arr(g, set())
d_arr, used = gen_arr(d, used)
f_arr, used = gen_arr(f, used)

# g_arr = [str(st) for st in range(1, g + 1)]
# d_arr = [str(st) for st in range(g + 1, g + d + 1)]
# f_arr = [str(st) for st in range(g + d + 1, g + d + f + 1)]
print(g, d, f)
print(' '.join(g_arr))
print(' '.join(d_arr))
print(' '.join(f_arr))