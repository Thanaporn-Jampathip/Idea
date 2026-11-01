from module import *

def main():
    TODO_FILE = 'todo.csv'
    # checkFile(TODO_FILE)
    while True:
        choice = input(f'{'Menu : To Do List':^30}\n{('='*30)}\n0. Exit\n1. Add\n2. Edit\n3. Done\n4. View All Todo\n5. Delete\n{('='*30)}\nSelect Choice : ')
        print()

        match choice : 
            case '0': print('Exit Program...'); break
            case '1': add(TODO_FILE)
            case '2': edit(TODO_FILE)
            case '3': statusDone(TODO_FILE)
            case '4': viewAll(TODO_FILE)
            case '5': delete(TODO_FILE)
        print()
if __name__ == '__main__': main()
