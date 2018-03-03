
g, d, f = list(map(int, input().split(' ')))

g_arr = list(map(int, input().split(' ')))
d_arr = list(map(int, input().split(' ')))
f_arr = list(map(int, input().split(' ')))

import itertools

count = 0
d_combos = list(itertools.combinations(d_arr, 2))
f_combos = list(itertools.combinations(f_arr, 3))
for gg in g_arr:
    for dd in d_combos:
        mx = max(gg, dd[0], dd[1])
        mn = min(gg, dd[0], dd[1])
        if mx / mn <= 2:
            for fff in f_combos:
                mx2 = max(mx, fff[0], fff[1], fff[2])
                mn2 = min(mn, fff[0], fff[1], fff[2])
                if mx2 / mn2 <= 2:
                    count += 1

print(count)
