import timeit

def NaiveGCD(a, b):
    gcd = 1
    for d in range(2, max(a,b)):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd

start_time = timeit.default_timer()
print(NaiveGCD(3918848,1653264))
print(timeit.default_timer() - start_time)

