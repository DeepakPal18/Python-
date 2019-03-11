num=int(input('enter any number...'))
print('the prime factors of {} are: ' .format (num))
d=2
while( num>1):
    if( num%d==0):
        print(d)
        num=num/d
        continue
    d=d+1
print('***********')
