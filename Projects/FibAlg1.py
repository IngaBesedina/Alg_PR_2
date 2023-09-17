import timeit
def FibRecursive(n):
	if n <= 1:
		return n
	else:
		return FibRecursive(n-1)+FibRecursive(n-2)

start_time = timeit.default_timer()
FibRecursive(40)
print(timeit.default_timer() - start_time)

