def primeNumbers(n):
    print(2)
    mid=int(n/2)
    values=2
    for i in range(mid):
        values+=i
        print(values)
print(primeNumbers(100))