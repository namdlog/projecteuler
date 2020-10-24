fib = [1,1]

for a in range(5000):
    fib += [(fib[len(fib)-1]+fib[len(fib)-2])]


print(len(fib[len(fib)-221])