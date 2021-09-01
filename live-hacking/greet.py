name = input('Name: ')
sex = input('Sex: ')
hour = int(input('Hour: '))

if hour <= 9:
    greeting = 'Good morning, '
elif hour > 9 and hour <= 17:
    greeting = 'Good day, '
elif hour > 17:
    greeting = 'Good evening, '

if sex == 'm':
    greeting += 'Mr. '
elif sex == 'f':
    greeting += 'Mrs. '

greeting += name

print(greeting)
