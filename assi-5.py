# Create a Dictionary of student Marks

dic1={'Sairaj':95,'Alice':85,'Viraj':92,'Rudresh':90}
a=str(input('Enter the student name :'))
b=a.capitalize()
if b in dic1:
    print(f'{b} marks :',dic1[b])
else:
    print('student not found.')


print('///------------------------------------------------------------------------------------------------------\\')


# Demonstrate List Slicing

l1=[1,2,3,4,5,6,7,8,9,10]
print('\n original list :',l1)
e=l1[0:5]
print('\n Extracted first five element :',e)
print('\n Reversed extracted elements :',e[::-1])