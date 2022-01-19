def multiply(*args):
    prod = 1
    for arg in args:
        prod*=arg
    return prod


print(multiply(1,2))
print(multiply(7,9,8,9,1,3,9,6,4,2))

def add(x,y):
    return x+y
# destructuring the li variable
li = [1,9]
print(add(*li))

def apply(*args,operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return "Not a Valid Operator"

print(apply(1,2,3,4,5,operator='*'))

# packing unpacking kwargs

def named(**kwargs):
    print(add(kwargs['x'],kwargs['y']))
    return kwargs

par = {'x':12,'y':14,'useles':'afsad'}

print(named(**par))

def named_2(a,b,c):
    print(a,b,c)

print("\tasdf")
temp = {
    'a':123,
    'b':'abcdefg',
    'c':['asdf','asdfv']
}
named_2(**temp)
