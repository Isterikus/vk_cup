n = int(input())

a = list(map(int, input().split()))
p = list(map(int, input().split()))


mn_x_arr = []
i = 0
while p:
	mn_x = p[0] ^ a[i]
	mn_j = 0
	j = 0
	for val in p:
		xr = val ^ a[i]
		if xr < mn_x:
			mn_x = xr
			mn_j = j
		j += 1
	del p[mn_j]
	i += 1
	mn_x_arr.append(mn_x)


print(" ".join(map(str,mn_x_arr)))
