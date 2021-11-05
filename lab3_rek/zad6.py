# def prime(n)-> bool:
#     if n == 0:
#         return  0
#     if n == 1:
#         return 1
#     else:
#         prime(n - 1)
#         if n == 0:
#             return False
#         else:
#             return True
#

def prime(n, i=2)-> bool:
    if (n < 2):
         return False
    if (n == 2):
        return True
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return prime(n, i + 1)


if prime(123):
    print("Yes")
else:
    print("No")