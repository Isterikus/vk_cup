max_dist = list(map(int, input().split(' ')))[1]
dst = list(map(int, input().split(' ')))

i = 0
steps = max_dist
change = 1
while i < len(dst):
    if i <= len(dst) - 2:
        if steps - (dst[i + 1] - dst[i]) >= 0:
            steps -= (dst[i + 1] - dst[i])
            i += 1
        elif steps < max_dist:
            change += 1
            steps = max_dist
        else: break
    elif i == len(dst) - 1:
        if steps >= 0: break
    else: break

if i >= len(dst) - 1: print(change)
else: print('-1')
