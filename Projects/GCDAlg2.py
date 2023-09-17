import timeit

def EuclidGCD(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return EuclidGCD(a % b, b)
    if b >= a:
        return EuclidGCD(a, b % a)
    
start_time = timeit.default_timer()
print(EuclidGCD(3918848, 1653264))
print(timeit.default_timer() - start_time)


