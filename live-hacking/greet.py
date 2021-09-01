import sys

name = input('Name: ')
sex = input('Sex: ')
hour = int(input('Hour: '))

# if hour in range(0, 10):    # <<<<< does not perform so well (linear search)
# if 0 <= hour and hour <= 9: # <<<<< unreadable but equivalent
if 0 <= hour <= 9:            # <<<<< best fit for our purpose
    greeting = 'Good morning, '
elif 10 <= hour <= 17:
    greeting = 'Good day, '
elif 18 <= hour <= 23:
    greeting = 'Good evening, '
else:
    print('error')
    sys.exit(1)

# if sex == 'm' or sex == 'M':
if sex in ('m', 'M'):
    greeting += 'Mr. '
elif sex in ('f', 'F'):
    greeting += 'Mrs. '
else:
    print('error')
    sys.exit(1)

greeting += name

print(greeting)
