import time

t0 = time.time()

lst = []


for i in range(1000):
	lst.append(0)

t1 = time.time()

total = t1-t0

print(total)