def caching_fibonacci() -> callable:
    """
    Create a Fibonacci function with memoization (caching).
    
    Returns a nested function that calculates Fibonacci numbers
    using a cache to store previously computed values for efficiency.
    
    Returns:
        callable: Fibonacci function with internal cache
    """

    cache = {}

    def fibonacci(n: int) -> int:
        """
        Calculate the nth Fibonacci number using memoization.
        
        Args:
            n (int): Position in the Fibonacci sequence (0-indexed)
            
        Returns:
            int: The nth Fibonacci number (0 if n <= 0)
        """

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

# Create Fibonacci function with cache
fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
