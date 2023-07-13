import time

def sum(n):
    start = time.time()

    res = 0
    for i in range(1, n+1):
        res += i
    
    end = time.time()

    return res, end-start

def fasterSum(n):
    start = time.time()

    res = n*(n+1)//2

    end = time.time()

    return res, end-start

for i in range(5):
    res, timeTaken = sum(100000)
    print(f"Sum: {res}. Time taken: {timeTaken}")

for i in range(5):
    res, timeTaken = fasterSum(100000)
    print(f"Sum: {res}. Time taken: {timeTaken}")