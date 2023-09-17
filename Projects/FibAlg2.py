import timeit

def FibArray(n):
    F = [0]*(n)
    F[0] = 0 
    F[1] = 1 
    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]
    return F[n - 1]


start_time = timeit.default_timer()
FibArray(40)
print(timeit.default_timer() - start_time)
