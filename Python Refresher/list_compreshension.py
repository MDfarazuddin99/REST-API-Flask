numbers = [1,2,3,4,5,6]
# single line
doubled_numbers = [x*2 for x in numbers]
print(doubled_numbers)

friends = ['Jake','Amy','Holt','Terry','Boyle','Hitckock']
filter_friends = [x for x in friends if x.startswith('H')]

print(filter_friends)


d_numbers = [(lambda x:x*2)(x) for x in numbers]

print(d_numbers)