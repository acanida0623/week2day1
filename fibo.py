def fib(n):    # write Fibonacci series up to n
    #create a doc string, you can view doc strings print(fibo.__doc__)
    """
    :param n: Tell us what n does
    """

    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n

    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


def fib3(n): # return Fibonacci series up to n
    a, b = 0, 1
    for m in range(n):
        a, b = b, a+b
    return b
