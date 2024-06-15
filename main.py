import os


def add_todo(data):
    num_todos = count_todos()
    with open('TODOs.txt', 'a') as file:
        file.write(f'{num_todos + 1}. {data} \n')

def count_todos():
    todo_count = 0
    with open('TODOs.txt', 'r') as file:
        for line in file:
            if line.strip().startswith(str(todo_count + 1) + '.'):
                todo_count += 1
    return todo_count


def delete_todo(number):
    todos = []
    with open('TODOs.txt', 'r') as file:
        for line in file:
            if not line.strip().startswith(f'{number}.'):
                todos.append(line)

    with open('TODOs.txt', 'w') as file:
        file.write(''.join(todos))
    renumber_todos()


def renumber_todos():
    with open('TODOs.txt', 'r') as file:
        lines = file.readlines()

    num_todos = count_todos()
    new_lines = []
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith(str(i) + '.'):
            new_lines.append(line)
        else:
            new_lines.append(f'{i}. {line.strip()[2:]}\n')

    with open('TODOs.txt', 'w') as file:
        file.write(''.join(new_lines))


def load_todos():
    with open('TODOs.txt', 'r') as file:
        return file.read()


choice = input('What do you want to do? N/L/D (New/Load/Delete): ')
if choice == 'N':
    data = input('Enter your TODO: ')
    add_todo(data)
elif choice == 'L':
    todos = load_todos()
    if todos:
        print(todos)
    else:
        print('No TODOs found.')
elif choice == 'D':
    number = input('Enter the number of the TODO you want to delete: ')
    delete_todo(number)
    print('TODO deleted successfully.')
else:
    print('Invalid choice')