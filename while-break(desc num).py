#print numbers in descending order, using break inside while:
x=int(input('enter a number ,from which, the descending order should start: '))
print(' number is : ',x)
#now enter a number at which you want to break the loop
y=int(input(' enter the num to break the loop: '))
print(' num: ',y)
while(x>0):
    print(' the number is {} ' .format(x))
    x=x-1
    if x==y:
        break
print(' ~~~~~loop breaks at {} ' .format(y))
