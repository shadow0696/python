#read a File and Handle Errors


#if the file exists:
with open('sample.txt','r') as f1:
    print('Reading file content')
    r1=f1.readline()
    print('\nLine1:',r1)
    r2=f1.readline()
    print('Line2:',r2)  

#if the file is not exist:
try:
    with open('sa.txt','r') as f1:
      print('Reading file content')
      r1=f1.readline()
      print('\nLine1:',r1)
      r2=f1.readline()
      print('Line2:',r2) 
except FileNotFoundError:
     print(f'\nError:The file {f1.name} was not found.')


#//...............................................................................\\


#Write and Append Data to File
w1=str(input("\nEnter text to write to file :"))
with open('output.txt','w') as f2:
    w=f2.write(w1)
    print(w)
    print(f"\nData successfully writen to {f2.name}")

    
w2=str(input("\nEnter additional text to append :"))
with open('output.txt','a') as f2:
    a=f2.writelines(w2)
    print(a)
    print(f"\nData successfully appended")

with open('output.txt','r') as f2:
    r=f2.read()
    print(f'\nFinal contant of {f2.name} :\n',r)
