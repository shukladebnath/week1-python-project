def fibonacci(n):
    """Print Fibonacci series values up to n."""
    a = 0
    b = 1

    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

    print()


def factorial(n):
    """Calculate and return the factorial of n."""
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def main():
    number = int(input("Enter a number (N): "))

    print("\nFibonacci series up to", number, ":")
    fibonacci(number)

    print("\nFactorial of", number, "is:", factorial(number))


if __name__ == "__main__":
    main()