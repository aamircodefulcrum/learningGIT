age = int(input('Enter Age:'))

if age >= 1 and age <=4:
    print('You are baby')

elif age >= 10  and age <= 20:
    print('You are Kid')

elif age >= 21 and age <= 34:
    print('You are Young')

elif age >= 35 and age <= 50:
    print('You are Man')

elif age >= 51 and age <= 120:
    print('You are Old')

else:
    print('You are not Human')
