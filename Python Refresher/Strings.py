# fstring -> It doesn't change dynamically
name = "faraz"

greeting = f"Hello, {name}"

print(greeting) # first instance

name = "tom"

print(greeting) #won't change dynamically

# Template strings using .format() method

greeting_ = "Hello, {}"
with_name1 = greeting_.format(name)
with_name2 = greeting_.format("any name cane be used like this")

print(with_name1)
print(with_name2)

