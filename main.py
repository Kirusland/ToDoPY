import os

def add_todo(data):
    with open('TODOs.txt', 'a') as file:
        num_todos = sum(1 for _ in file)
        file.write(f'\n{num_todos + 1}. {data}')

def load_todos():
    with open('TODOs.txt', 'r') as file:
        return file.read()

choice = input('What do you want to do? N/L (New/Load): ')
if choice == 'N':
    data = input('Enter your TODO: ')
    add_todo(data)
elif choice == 'L':
    todos = load_todos()
    if todos:
        print(todos)
    else:
        print('No TODOs found.')
else:
    print('Invalid choice')