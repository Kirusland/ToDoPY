import os

choice = input('What do you want to do? N/L (New/Load): ')
if choice == 'N':
    file = open('TODOs.txt', 'a')
    data = input('Enter your TODO: ')
    if os.path.exists('TODOs.txt') and os.path.getsize('TODOs.txt') > 0:
        file.write('\n' + data)
    else:
        file.write(data)

elif choice == 'L':
    file = open('TODOs.txt', 'r')
    print(file.read())
else:
    print('Invalid choice')