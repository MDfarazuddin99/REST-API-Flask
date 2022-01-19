def divide(dividend=12, divisor=3):
    if divisor!=0:
        return dividend/divisor
    else:
        return 'ZERO DIVISION ERROR'

# Positional arguments should come before key-worded arguments
print(divide())
