#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip = float(input("How much tip would you like to give? 10 , 12, or 15?"))
total_tip = tip/100
total_bill = round(bill*total_tip + bill,2)#"{:.2f}".format can be used
print(f"total bill with tip: {total_bill}")
ppl = int(input("number of ppl to split the bill in? "))
#pay = round(total_bill/ppl,2)#will give single decimal place if bill is whole number eg-150,100
pay = "{:.2f}".format(total_bill/ppl)#formating 2 places after decimal
print(f"each one have to pay: {pay}")