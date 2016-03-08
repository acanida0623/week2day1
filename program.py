import fibo

print (fibo.fib(2000))




#enumerate returns each item as a tupell


for i, n in enumerate(fibo.fib2(1000)):


    print("{0}: {1}".format(i,n,))

    #The {0} and {1} are indexes of the enumerate values that i had place in the format method. {2} is going to print i



#take ninthe fibo number and divide it by the eigth
"""def nth_quot(n):
    fibos = []
    for i, x in enumerate(fibo.fib2(1000000000)):
        fibos.append(x)
    answer = fibos[n-1] / fibos[n-2]
    return answer

print (nth_quot(9))"""


def nth_quot2(n):
    answer = fibo.fib3(n) / fibo.fib3(n-1)
    return answer


print (fibo.fib3(2000))
print (fibo.fib3(1999))
print (nth_quot2(2000))
