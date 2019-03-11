sub=0
marks=0
total=0
while(sub<6):
   sub=sub+1
   marks=int(input('enter marks for sub{}:' .format(sub)))
   total=total+marks
avg=total/sub
print('avg marks are {}:' .format(avg))
