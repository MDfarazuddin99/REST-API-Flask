def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("You dumb fuck! the divisor can't be 0")
    else:
        return dividend/divisor

dividend,divisor = list(map(int,input("Enter dividend, divisor [space seperated]").split()))

try:
    print(divide(dividend,divisor))
except ZeroDivisionError:
    print('your ass should be fucked!')