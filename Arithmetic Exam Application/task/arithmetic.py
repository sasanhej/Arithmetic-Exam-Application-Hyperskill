import random


def simple():
    mark = 0
    for i in range(5):
        op = random.choice(['-', '+', '*'])
        fd = random.randint(2, 9)
        sd = random.randint(2, 9)
        ex = f'{fd} {op} {sd}'
        print(ex)
        while True:
            answer = input()
            if len(answer) > 0:
                if answer.isdigit():
                    ans = int(answer)
                    break
                elif len(answer)>1:
                    if answer[0]=='-':
                        if answer[1:].isdigit():
                            ans = int(answer)
                            break
            print("Incorrect format.")
        rans = eval(ex)
        if ans == rans:
            print('Right!')
            mark += 1
        else:
            print('Wrong!')
    return mark


def square():
    mark = 0
    for i in range(5):
        fd = random.randint(11, 29)
        print(fd)
        while True:
            answer = input()
            if len(answer) > 0:
                if answer.isdigit():
                    ans = int(answer)
                    break
                elif len(answer)>1:
                    if answer[0]=='-':
                        if answer[1:].isdigit():
                            ans = int(answer)
                            break
            print("Incorrect format.")
        rans = fd**2
        if ans == rans:
            print('Right!')
            mark += 1
        else:
            print('Wrong!')
    return mark

def choose():
    promp = f'Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n'
    while True:
        answer = input(promp)
        if len(answer) > 0:
            if answer.isdigit():
                if int(answer) in [1,2]:
                    mod = int(answer)
                    break
        print("Incorrect format.")
    return mod


mod = choose()
if mod == 1:
    lvl = 'simple operations with numbers 2-9'
    mark = simple()
else:
    lvl = 'integral squares of 11-29'
    mark = square()
save = input(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
if save in ['yes', 'YES', 'y', 'Yes']:
    name = input('Enter username:')
    results = open('results.txt', 'a')
    results.writelines(f'{name}: {mark}/5 in level {mod} ({lvl})')
    results.close()
    print('The results are saved in "results.txt".')