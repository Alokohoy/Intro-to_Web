#square of a number
def square(num):
    return num ** 2

print("square of 5:", square(5))

#list of numbers
def sum_list(numbers):
    return sum(numbers)

print("Sum of [1, 2, 3, 4, 5]:", sum_list([1, 2, 3, 4, 5]))

#number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?:", is_prime(7))
print("Is 10 prime?:", is_prime(10))

#Fibonacci sequence

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
