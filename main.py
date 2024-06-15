choice = input('What do you want to do? N/L (New/Load): ')
if choice == 'N':
    file = open('TODOs.txt', 'a')
    data = input('Enter your TODO: ')
    file.write('\n'+data)
elif choice == 'L':
    file = open('TODOs.txt', 'r')
    print(file.read())
else:
    print('Invalid choice')