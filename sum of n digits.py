# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(type(two_digit_number))
sum = int(two_digit_number[0]) + int(two_digit_number[1])
#sum = int(two_digit_number[0] + two_digit_number[1])
#above line gives "int obj not subscriptable error"
print(type(sum))
print(sum)
char_sum = str(sum)
print("sum of the 2 digits will be: " + char_sum)

#Sum of n digit input-
x = input("Type a number: ")
print(f"number of digits in input: {len(x)}")
sum = 0
for char in range (len(x)):
  sum += int(x[char])
print(f"sum of {len(x)} digit input is: {sum}") 
  




