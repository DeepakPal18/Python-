num=int(input('enter a number..'))
fact=1
for x in range(1,num+1):
    fact=fact*x
print(' factorial of {} is: {}' .format( num,fact))
