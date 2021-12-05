def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    r_num = []
    for i in range(3):
        n = int(input())
        r_num.append(n)
    age = (r_num[0] * 70 + r_num[1] * 21 + r_num[2] * 15) % 105
    print("Your age is", age, "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr += 1


def test(qu, an):
    index = 0
    qu_num = 1
    print("Let's test your programming knowledge.")
    for i in range(len(qu)):
        print(str(qu_num) + ". ", qu[index])
        qu_num += 1
        index += 1
    b = int(input())
    while b != ans:
        print("Please, try again.")
        b = int(input())            
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Yoda', '2021')  # change it as you need
remind_name()
guess_age()
count()
a = ["To repeat a statement multiple times.", "To decompose a program into several small subroutines.", "To determine the execution time of a program.", "To interrupt the execution of a program."]
ans = 2
test(a, ans)
end()
