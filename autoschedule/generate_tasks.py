def read_file():
    # Read lines from tasks_layout.txt
    with open("tasks_layout.txt", "r") as b:
        k = b.readlines()[3:]
    return k

def remove_formatting(List):
    # Remove formatting from the list of tasks
    m = [i.replace('\n', '').split(' ') for i in List if '#' not in i]
    return m

def strings_to_ints(List):
    # Converts strings to integers (some parameters, to be specified)
    l = [[int(j[0]), j[1], int(j[2])] for j in List]
    return l

def ints_to_weight(List):

    # convert integer at end of line to weight
    # 1 = 4
    # 2 = 2
    # 4 = 1
    # else: encountered a non-conforming weight

    a = List
    b = []
    for i in a:
        if i[0] == 1:
            b.append([4,i[1],i[2]])
        elif i[0] == 2:
            b.append(i)
        elif i[0] == 3:
            print('Encountered a non-conforming weight')
        elif i[0] == 4:
            b.append([1,i[1],i[2]])
        else:
            print('Encountered a non-conforming weight')
    return b

def tasks_with_weights(List):
    # generate tasks with weights
    a = List
    b = []
    for i in a:
        for j in range(i[2]):
            b.append(i[:2])
    return b


def weight_of_group(group):
    # return total weight of a group of tasks
    a = 0
    for i in group:
        a += i[0]
    return a

def weight_less(group):
    # return True if weight of group is less than 4 otherwise False
    b = weight_of_group(group)
    if b < 4:
        return True
    else:
        return False


def loadable(group, task):
    # return False if a group is filled (total weight == 4) otherwise True
    if weight_of_group(group) + task[0] <= 4:
        return True
    else:
        return False


def group_to_weight4(List):
    # group tasks into 4-weight list
    a = List
    b = [[]]
    for i in a:
        k = len(b)
        for j in range(k):
            if weight_less(b[j]):
                if loadable(b[j], i):
                    b[j].append(i)
                    break
                else:
                    if j == k-1:
                        b.append([i])
                        break
            else:
                if j < k-1:
                    pass
                else:
                    b.append([i])
                    break
    return b



def shuffle_tasks(my_tasks):
    # Shuffle and group tasks
    m = copy.deepcopy(my_tasks)
    undecided = True
    for i in m:
        print(i)
    n = group_to_weight4(m)
    while undecided:
        k = input('Would you like to shuffle and group tasks?(y/n)\n')
        if k == 'y':
            random.shuffle(m)
            n = group_to_weight4(m)
            for i in range(len(n)):
                print(str(i + 1) + ' ' + str(n[i]))
        elif k == 'n':
            k = input('Would you like to exit?(y/n)\n')
            if k == 'y':
                undecided = False
                return n
            if k == 'n':
                pass
        else:
            print('Invalid input. Try again\n')


def write_tasks_to_file(my_tasks, date_today):
    # Write tasks to tasks_list.txt
    with open("tasks_list.txt", "w") as my_file:
        my_file.writelines('#Each task > 2 letters\n' + '20' + date_today.strftime("%y") + ', '+ date_today.strftime("%m") + ' , ' + date_today.strftime("%d") + '\n')
        k = 1
        j = 1
        space = ''
        for i in my_tasks:
            if k > 9:
                space = ' '
            if len(i) == 1:
                my_file.writelines(str(k) + '---->' + str(i[0][0]) + '<----->'+ str(j)+ '. ' + i[0][1] + '\n\n')

                k += 1
                j += 1

            elif len(i) == 2:
                h = str(k) + '---->' + str(i[0][0]) + '<----->'+ str(j)+ '. ' \
                + i[0][1] + '\n ' + space + '---->' + str(i[1][0]) + '<----->'+ str(j + 1) + '. ' \
                + i[1][1] + '\n\n'
                my_file.writelines(h)
                k += 1
                j += 2

            if len(i) == 3:
                h = str(k) + '---->' + str(i[0][0]) + '<----->'+ str(j)+ '. ' \
                + i[0][1] + '\n ' + space + '---->' + str(i[1][0]) + '<----->'+ str(j + 1) + '. ' \
                + i[1][1] + '\n ' + space + '---->' + str(i[2][0]) + '<----->'+ str(j + 2)+ '. ' \
                + i[2][1] + '\n\n'
                my_file.writelines(h)
                k += 1
                j += 3

            elif len(i) == 4:
                h = str(k) + '---->' + str(i[0][0]) + '<----->'+ str(j)+ '. ' \
                + i[0][1] + '\n ' + space + '---->' + str(i[1][0]) + '<----->'+ str(j + 1) + '. ' \
                + i[1][1] + '\n ' + space + '---->' + str(i[2][0]) + '<----->'+ str(j + 2)+ '. ' \
                + i[2][1] + '\n ' + space + '---->' + str(i[3][0]) + '<----->'+ str(j + 3) + '. ' \
                + i[3][1] + '\n\n'
                my_file.writelines(h)
                k += 1
                j += 4
    print('Writing tasks done! Your tasks are now in tasks_list.txt\n')



if __name__ == "__main__":
    from IPython.display import clear_output
    from datetime import date
    import random
    import  copy
    d_tod = date.today()
    unshuffled_Tasks = tasks_with_weights(ints_to_weight(strings_to_ints(remove_formatting(read_file()))))
    shuffled_Tasks = shuffle_tasks(unshuffled_Tasks)
    undecided = True
    while undecided:
        k = input('Nice job creating Tasks :) Would you like to save them?(y/n)\n')
        if k == 'y':
            write_tasks_to_file(shuffled_Tasks, d_tod)
            undecided = False
        elif k == 'n':
            k = input('Would you like to exit?(y/n)\n')
            if k == 'y':
                undecided = False
            if k == 'n':
                pass
        else:
            print('Invalid input. Try again\n')
