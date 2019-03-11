#prime number program using break with for loop
x=int(input('enter a number: '))
print('entered number is: ',x)
for i in range(2,x):
    if x%i==0:
        print('{} is not a prime number.' .format(x))
        break
else:
     print('{} is a prime number.' .format(x))
