# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill=0
 
if size=='S':
    if add_pepperoni == 'Y':
        bill = 17
    
elif size == 'M':
    if add_pepperoni =='Y':
        bill=23
elif size == 'L':
    if add_pepperoni=='Y':
        bill=28
if extra_cheese == 'Y':
    bill=bill+1

print(bill)

        