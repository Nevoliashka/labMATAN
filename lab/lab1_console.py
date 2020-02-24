import re


def string_to_array(string):
    pattern_int = r'(?<![-.])\b[0-9]+\b(?!\.[0-9])|[Ø]'
    pattern_float = r'[-+]?\d+[.]\d+'
    array_float = re.findall(pattern_float, string)
    array_int = re.findall(pattern_int, ' ' + string + ' ')
    array = []
    array += list(map(lambda x: int(x), array_int))
    array += list(map(lambda x: float(x), array_float))
    if not array:
        array.append('Ø')
    else:
        array.sort()
    return array


message = '''Press 1 - to enter set A  
Press 2 - to enter set B
Press 3 - to show Union
Press 4 - to show Difference A\\B
Press 5 - to show Difference B\\A
Press 6 - to show Intersection
Press 7 - to show Symmetric difference 
Press 8 - to exit
'''
A = set('Ø')
B = set('Ø')

while (1):
    print(message)
    number = input()
    if number == "1":
        A = string_to_array(input())
        print("A = {}".format(set(A)))
    elif number == "2":
        B = string_to_array(input())
        print("B = {}".format(set(B)))
    elif number == "3":
        print("Union = {}".format(set(A+B)))
    elif number == "4":
        print("Difference A\\B = {}".format(set(A) - set(B) or set('Ø')))
    elif number == "5":
        print("Difference B\\A = {}".format(set(B) - set(A) or set('Ø')))
    elif number == "6":
        print("Intersection = {}".format(set(set(A+B)) - set(list((set(B) - set(A) or set('Ø'))) + list(set(A) - set(B) or set('Ø')))) or set('Ø'))
    elif number == "7":
        print("Symmetric difference = {}".format(set(list((set(B) - set(A) or set('Ø'))) + list(set(A) - set(B) or set('Ø')))))
    elif number == "8":
        break
