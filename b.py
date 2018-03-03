passengers = list(map(int, input().split(' ')))[1]

def parsePlane(plane):
    d = {0: [], 1: [], 2: []}
    for col in range(0, len(plane)):
        for row in range(0, len(plane[col])):
            for place in range(0, len(plane[col][row])):
                if plane[col][row][place] == '.':
                    if place == 0:
                        if plane[col][row][place + 1] == 'S': d[1].append([col, row, place])
                        else: d[0].append([col, row, place])
                    elif place == len(plane[col][row]) - 1:
                        if plane[col][row][place - 1] == 'S': d[1].append([col, row, place])
                        else: d[0].append([col, row, place])
                    else:
                        n = 0
                        if plane[col][row][place + 1] == 'S': n += 1
                        if plane[col][row][place - 1] == 'S': n += 1
                        d[n].append([col, row, place])

    return d



plane = []
while True:
    try: plane.append([list(x) for x in input().split('-')])
    except: break

plane = list(map(list, zip(*plane)))
d = parsePlane(plane)

for best in d.values():
    if passengers == 0: break
    for place in best:
        if passengers == 0: break
        plane[place[0]][place[1]][place[2]] = 'x'
        passengers -= 1

res = ''
for rows in list(zip(*plane)):
    for row in range(0, len(rows)): res += ''.join(rows[row]) + ('-', '')[row == len(rows) - 1]
    res += '\n'

total = 0
for i in range(0, len(res)):
    if res[i] == 'S':
        try: total += (0, 1)[res[i - 1] != '.' and res[i - 1] != '-' and res[i - 1] != '\n']
        except: pass
        try: total += (0, 1)[res[i + 1] != '.' and res[i + 1] != '-' and res[i + 1] != '\n']
        except: pass

print(total)
print(res, end='')