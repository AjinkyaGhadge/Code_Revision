def recursive_fibonacci(n):
    if n<=1:
        return 1
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)