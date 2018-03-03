n, s, f = list(map(int, input().split(' ')))
gates_col = list(map(int, input().split(' ')))
gates_keys = list(map(int, input().split(' ')))

keys_exist = set()
s -= 1
f -= 1

# keys_need = set(gates_keys[min(s, f): max(s, f) + 1])
# keys_have = set(gates_col[min(s, f): max(s, f)])

# def count_keys_need(i, j):
keys_need = set(gates_keys[min(s, f): max(s, f) + 1])
keys_have = set(gates_col[min(s, f): max(s, f)])
print(keys_need)
print(keys_have)

# while True:
    # keys_exist.add(gates_keys[now])
