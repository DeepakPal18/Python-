x=int(input("enter a number: "))
if x%2==0:      # bewARE of whitespacing..
      if x%3==0:
       print("number divisible by 2 and 3 ")
      else:
       print("number is divisible by only 2 ")
else:
      if x%3==0:
       print(" number is divisible by 3 only")
      else:
       print(" number is not divisible by 2 and 3")
