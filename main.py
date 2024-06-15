import os

choice = input('What do you want to do? N/L (New/Load): ')
file_exists = os.path.exists('TODOs.txt') and os.path.getsize('TODOs.txt') > 0

if choice == 'N':
    with open('TODOs.txt', 'a') as file:
        data = input('Enter your TODO: ')
        if file_exists:
            file.write('\n' + data)
        else:
            file.write(data)
elif choice == 'L':
    with open('TODOs.txt', 'r') as file:
        print(file.read())
else:
    print('Invalid choice')