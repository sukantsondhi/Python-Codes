a=int(input('How many numbers: '))
sum=0
for i in range(a):
    numbers=float(input('Enter no: '))
    sum+=numbers
avg=sum/a
print('The Avg of these',a,'numbers is: ',avg)
