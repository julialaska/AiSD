def numbers(n):
    if n < 0:
        return
    else:
        print(n)
        return numbers(n - 1)

numbers(10)