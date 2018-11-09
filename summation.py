import math
import time

# a:list = []
print("creating list")
a = range(1000000000)
print("done creating list")


def iterative_sum(a):
    sum = 0
    for el in a:
        sum += el
    return sum


def binary_sum(a, i, n):
    if n == 1:
        return a[i]
    return binary_sum(a, i, math.ceil(n/2)) + binary_sum(a, i + math.ceil(n/2), int(n/2))


print("built in sum()")
start = time.time()
print(sum(a))
end = time.time()
print(end - start, "\n")

print("iterative sum")
start = time.time()
print(iterative_sum(a))
end = time.time()
print(end - start, "\n")

print("recursive sum")
start = time.time()
print(binary_sum(a, 0, len(a)))
end = time.time()
print(end - start, "\n")