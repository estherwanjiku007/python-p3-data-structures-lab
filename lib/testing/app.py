fibonacci_seq={}
def fibonacci(n):
    if n in fibonacci_seq:
        return fibonacci_seq[n]
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        value=fibonacci(n-1) +fibonacci(n-2)
        fibonacci_seq[n]=value
    return value
    
for n in range(1,10):
    print(n ,":",fibonacci(n))