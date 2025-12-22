a=int(input('enter the 1st number:'))
b=int(input('enter the 2nd number:'))
c=int(input('enter the 3rd number:'))
d=int(input('enter the 4th number:'))
if a>b:
    if a>c:
         if a>d:
            print('a is greatest')
         else:
            print('d is greatest')
else:
    if b>c:
        print('b is greatest')
    else:
        print('c is greatest')
    else:
        print('d is smaller')

