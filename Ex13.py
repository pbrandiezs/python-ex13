
def next_fib(fib_list):
    return(fib_list[-1] + fib_list[-2])

how_many = input("How many fibonacci's in the sequence would you like? ")
how_many = int(how_many)

for I in range(1,(how_many + 1)):
    if I == 1:
        fibonacci = [1]
    if I == 2:
        fibonacci = [1, 1]
    if I >= 3:
        fibonacci.append(next_fib(fibonacci))

print(fibonacci)


