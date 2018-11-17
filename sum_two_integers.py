a = [1, 3, 5, 7, 9, 10, 11, 12, 13]

def sum_v(a, v):
    """
    Checks if any two integers in a can add up to make v.
    
    Design an algorithm that takes a sorted array of integers,
    called A, of size n and an integer value, called v.
    The algorithm should determine if there are two integers in A
    whose sum is equal to v. (e.g.A[i] + A[j] = v, where i < nandj < n.)

    This is a proof of concept for a past exam practice for university subject.
    This should run in O(n) time-complexity assuming a constant time for
    map dict operations.
    """
    dict = {}
    for x in a:
        y = v - x
        if y in dict.keys():
            print("v =",y, "+", x)
            return True
        dict[x] = "x"
    return False

print(sum_v(a, 15))
print(sum_v(a, 18))
print(sum_v(a, 2))
