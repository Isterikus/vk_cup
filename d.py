n, s, f = list(map(int, input().split(' ')))
gates_col = list(map(int, input().split(' ')))
gates_keys = list(map(int, input().split(' ')))

keys_exist = set()
s -= 1
f -= 1
now = s

keys_need = set(gates_keys[min(s, f): max(s, f) + 1])

while True:
    keys_exist.add(gates_keys[now])
