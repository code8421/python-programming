cache = [0] * 8

def fibo(x):
    if x <= 2:
        return 1
    
    if cache[x] != 0:
        return cache[x]
    
    else:
        cache[x] = fibo(x - 1) + fibo(x - 2)
    
    return cache[x]

print(fibo(7))
