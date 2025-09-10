def matemaatilised_arvutused(a, b):
    summa = a + b
    vahe = a - b
    jagatis = a // b
    korrutis = a * b

    return summa, vahe, jagatis, korrutis

print(matemaatilised_arvutused(10, 5))
# oodatav vastus: (15, 5, 2, 50)

summa, vahe, jagatis, korrutis = matemaatilised_arvutused(10, 5)
# test
assert summa == 15
print("Summa on õige")
assert vahe == 5
print("Vahe on õige")
assert jagatis == 2
print("Jagatis on õige")
assert korrutis == 50
print("Korrutis on õige")