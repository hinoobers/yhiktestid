def matemaatilised_arvutused(a, b):
    summa = a + b
    vahe = a - a
    jagatis = a // b
    korrutis = a * a

    return summa, vahe, jagatis, korrutis

print(matemaatilised_arvutused(10, 5))
# oodatav vastus: (15, 5, 2, 50)