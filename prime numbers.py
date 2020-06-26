def numbers(num):
    prime=0
    for val in range(2, int(num+1)):
        if all(val%int!=0 for int in range(2, val)):
            prime+=1
    return prime
n=int(input('Enter the number:'))
print('2 to',n,'prime numbers there are:',numbers(n),'numbers')