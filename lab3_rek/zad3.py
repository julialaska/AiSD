def  power(number: int, n: int) -> int:
    if n==0:
        return 1
    elif n ==1:
        return number
    else:
        return number*pow(number,n-1)

print(power(2,4))