a=int(input('enter how many elements of fibonacci series do you want: '))
first=0
second=1
print(first)
print(second)
for i in range (1,a+1):
    third=first+second
    print(third)
    first,second=second,third
