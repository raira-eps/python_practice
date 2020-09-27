s,g = [int(i) for i in input().split()]
seats = [False] * s
for j in range(g):
    n,init = [int(i)for i in input().split()]
    if not True in seats[init-1:init+n-1]:
        seats[init-1:init+n-1] = [True] * n
print(seats.count(True))