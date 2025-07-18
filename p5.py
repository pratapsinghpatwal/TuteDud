def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


sample_number = int(input("Enter a number:   "))
fact = factorial(sample_number)

print(f"The factorial of {sample_number} is: {fact}")
