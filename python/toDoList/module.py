import csv, os

def add(filename):
    print('< Add Todo >')
    name = input('Enter name to do : ')
    level_priority = input('Enter priority (l = low, m = medium, h = high ) : ')

    if level_priority == 'l': priority = 'low'
    elif level_priority == 'm' : priority = 'medium'
    elif level_priority == 'h' : priority = 'high'
    else: 'not have this level priority'

    if os.path.exists(filename):
        with open(filename, 'r' , encoding='utf-8') as f:
            line_count = len(f.readlines())
    else:
        line_count = 0

    todo_id = line_count + 1

    with open(filename, 'a', encoding='utf-8') as f:
        f.writelines(f'{todo_id},{name},{priority},{'pending'}\n')
    print()
    print('Add todo success..')

def edit(filename):
    print(f'{'All To Do List':^65}\n{('='*65)}\n|{'Id':^5}|{'Name':^30}|{'Priority':^15}|{'Status':^10}|\n{('='*65)}')

    with open(filename, 'r') as f:
        data = f.readlines()

    for n in range(len(data)):
        parts = data[n].strip().split(',')

        id = parts[0]
        name = parts[1]
        priority = parts[2]
        status = parts[3]

        print(f'|{id:^5}| {name:<29}|{priority:^15}|{status:>9} |')
    print('='*65)
    print()
    print('< Edit Todo >')
    id_select = input('Enter Id : ')

    for i in range(len(data)):
        parts = data[i].strip().split(',')

        id_inData = parts[0]

        # check id have or not have
        found = False
        if id_select == id_inData: found = True; indexFound = i; break

    if found:
        # print(indexFound) # check id
        parts = data[indexFound].strip().split(',') # old data

        old_name = parts[1]
        old_priority = parts[2]
        
        need_edit = input(f'What field you need to edit ? (n = name, p = priority, ) : ')
        if need_edit == 'n':
            new_name = input(f'Enter new name at id {id_select} : ')
            
            data[indexFound] = f'{id_select},{new_name},{old_priority},pending\n'

            with open(filename, 'w', encoding='utf-8')as f:
                f.writelines(data)

            print()
            print(f'Edit name of id {id_select} success..')
            print()
            print(f'{'All To Do List':^65}\n{('='*65)}\n|{'Id':^5}|{'Name':^30}|{'Priority':^15}|{'Status':^10}|\n{('='*65)}')
            for f in range(len(data)):
                parts = data[f].strip().split(',')
        
                id = parts[0]
                name = parts[1]
                priority = parts[2]
                status = parts[3]
        
                print(f'|{id:^5}| {name:<29}|{priority:^15}|{status:>9} |')
            print('='*65)

        elif need_edit == 'p':
            level_priority = input(f'Enter new priority at id {id_select} (l = low, m = medium, h = high ) : ')
            
            if level_priority == 'l': new_priority = 'low'
            elif level_priority == 'm' : new_priority = 'medium'
            elif level_priority == 'h' : new_priority = 'high'
            else: 'not have this level priority'

            data[indexFound] = f'{id_select},{old_name},{new_priority},pending\n'

            with open(filename, 'w', encoding='utf-8')as f:
                f.writelines(data)

            print()
            print(f'Edit priority of id {id_select} success..')
            print()
            print(f'{'All To Do List':^65}\n{('='*65)}\n|{'Id':^5}|{'Name':^30}|{'Priority':^15}|{'Status':^10}|\n{('='*65)}')
            for f in range(len(data)):
                parts = data[f].strip().split(',')
        
                id = parts[0]
                name = parts[1]
                priority = parts[2]
                status = parts[3]
        
                print(f'|{id:^5}| {name:<29}|{priority:^15}|{status:>9} |')
            print('='*65)
            
        else:
            print('not have choice edit please select choice again..')
    else:
        print(f'not have id {id_select}')

def statusDone (filename):
    print(f'{'All To Do List':^65}\n{('='*65)}\n|{'Id':^5}|{'Name':^30}|{'Priority':^15}|{'Status':^10}|\n{('='*65)}')
    
    with open(filename, 'r') as f:
        data = f.readlines()

    for n in range(len(data)):
        parts = data[n].strip().split(',')

        id = parts[0]
        name = parts[1]
        priority = parts[2]
        status = parts[3]

        print(f'|{id:^5}| {name:<29}|{priority:^15}|{status:>9} |')
    print('='*65)
    print()
    print('< Change Status Pending to Done >')
    id_select = input('Enter Id : ')
    
    for i in range(len(data)):
        parts = data[i].strip().split(',')

        id_inData = parts[0]

        # check id have or not have
        found = False
        if id_select == id_inData: found = True; indexFound = i; break

    if found:
        parts = data[indexFound].strip().split(',')
        name_inData = parts[1]
        priority_inData = parts[2]
        # change status pending to done from id user select
        data[indexFound] = f'{id_select},{name_inData},{priority_inData},done\n'
        # update in database 
        with open(filename, 'w') as f:
            f.writelines(data)
        # show updated data
        print()
        print(f'change status of id {id_select} success..')
        print()
        print(f'{'All To Do List':^65}\n{('='*65)}\n|{'Id':^5}|{'Name':^30}|{'Priority':^15}|{'Status':^10}|\n{('='*65)}')
        for f in range(len(data)):
            parts = data[f].strip().split(',')
    
            id = parts[0]
            name = parts[1]
            priority = parts[2]
            status = parts[3]
    
            print(f'|{id:^5}| {name:<29}|{priority:^15}|{status:>9} |')
        print('='*65)
    else:
        print(f'not have id {id_select}')
    

def viewAll(filename):
    print('< View All Todo >')
    with open(filename, 'r') as f:
        data = f.readlines()

    print(f'{'All To Do List':^65}\n{('='*65)}\n|{'Id':^5}|{'Name':^30}|{'Priority':^15}|{'Status':^10}|\n{('='*65)}')
    for n in range(len(data)):
        parts = data[n].strip().split(',')

        id = parts[0]
        name = parts[1]
        priority = parts[2]
        status = parts[3]

        print(f'|{id:^5}| {name:<29}|{priority:^15}|{status:>9} |')
    print('='*65)

def delete(filename):
    print(f'{'All To Do List':^65}\n{('='*65)}\n|{'Id':^5}|{'Name':^30}|{'Priority':^15}|{'Status':^10}|\n{('='*65)}')
        
    with open(filename, 'r') as f:
        data = f.readlines()

    for n in range(len(data)):
        parts = data[n].strip().split(',')

        id = parts[0]
        name = parts[1]
        priority = parts[2]
        status = parts[3]

        print(f'|{id:^5}| {name:<29}|{priority:^15}|{status:>9} |')
    print('='*65)
    print()
    print('< Delete Todo >')
    id_select = input('Enter Id : ')
    
    for i in range(len(data)):
        parts = data[i].strip().split(',')

        id_inData = parts[0]

        # check id have or not have
        found = False
        if id_select == id_inData: found = True; indexFound = i; break

    if found:
        confirm = input(f'You really delete id {id_select} ? (y/n) : ')
        if confirm == 'y':
            data.pop(indexFound)

            for o in range(len(data)):
                parts = data[o].strip().split(',')
                parts[0] = str(o + 1)
                data[o] = ','.join(parts) + '\n'

            with open(filename, 'w') as f:
                f.writelines(data)
            print()
            print(f'Delete id {id_select} success..')
            print()
        else:
            print()
            pass

        print(f'{'All To Do List':^65}\n{('='*65)}\n|{'Id':^5}|{'Name':^30}|{'Priority':^15}|{'Status':^10}|\n{('='*65)}')
        for f in range(len(data)):
            parts = data[f].strip().split(',')
    
            id = parts[0]
            name = parts[1]
            priority = parts[2]
            status = parts[3]
    
            print(f'|{id:^5}| {name:<29}|{priority:^15}|{status:>9} |')
        print('='*65)

    else:
        print(f'Not found id {id_select}')