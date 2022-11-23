A=int(input('enter an integer(>1000): '))
reverse=0
a=A
while a:
    digit=a%10
    a=a//10
    reverse=reverse*10+digit
print('reverse of',A,'is',reverse)
    
