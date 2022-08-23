L = ["Python", 1, True, False, "Java"]
L1 = list(range(10))
print(L)
print(L1)
print("Python" in L)
print(10 in L1)
L[len(L):] = ["Hello World"]
print(L)
print(L[-1:-1])
L[-1:] = []
print(L[-1:])
print(L)
L.insert(2,3)
print(L)
print(L.pop())
L[1:3] = [2,4]
print(L)
# L[:] = []
# print(L)
# L = L[-1::-1]
# print(L)
print(L[:0])
print(L[-1:])

L2 = list(range(10))
print(L2)
L3 = L + L2
print(L3)
print(L2 * 2)
