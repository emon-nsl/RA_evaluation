def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

n_list = input("Please enter how many fibonacchi series you want ")
nums = n_list.split(',')
# print(num)

for n in nums:
    print(list(fibonacci_generator(int(n))))