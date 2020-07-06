a='a'
b='b'
c='c'
d='d'
e='e'
f='f'
g='g'
h='h'
i='i'
grid = f'''|{a}|{b}|{c}|
|{d}|{e}|{f}|
|{g}|{h}|{i}|'''

goes_first=input('Would you like to go first? y/n')
condition1 = a == b and b == c
condition2 = d == e and e == f
condition3 = g == h and h == i
condition4 = a == d and d == g
condition5 = b == e and e == h
condition6 = c == f and f == i
condition7 = a == e and e == i
condition8 = c == e and e == g
conditionlist = {condition1, condition2, condition3, condition4, condition5, condition6, condition7, condition8}
if goes_first == 'n':
    while not condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7 or condition8:
        compute_list={i,h,g,f,e,d,c,b,a}
        for i in compute_list:
            if i != 'O' or i != 'X':
                i = 'O'
                break
        user_input=input(f'Which grid would you like to place your mark?\n{grid}')
        for i in compute_list:
            if user_input = i:
                i='X'
