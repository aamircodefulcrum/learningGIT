age = int(input('Enter Age:'))

if age > 1 and age < 4:
    print('You are baby')

elif age > 10  and age < 20:
    print('You are Kid')

elif age > 20 and age < 35:
    print('You are Young')

elif age > 34 and age < 51:
    print('You are Mid Aged')

elif age > 50 and age < 121:
    print('You are Old')

else:
    print('You are not Human')
