
#check if a number is even or odd
a=int(input("Enter a number:"))
if a%2==0:
   print(f"{a} is an even number")
else:
   print(f"{a} is an odd number")




#sum of integer from 1 to 50 Using a loop
l=0
for i in range(1,51):
   l += i
print("\nThe sum of number from 1 to 50 is:",l)      