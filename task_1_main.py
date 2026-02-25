def caching_fibonacci():
    caсhe = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in caсhe:
            return caсhe[n]
        caсhe[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return caсhe[n]
    return fibonacci


fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
