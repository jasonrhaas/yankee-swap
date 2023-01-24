import random
import string
from collections import OrderedDict


def translate(letter):
    fun = list(string.ascii_lowercase)
    num = fun.index(letter)
    return num


names = [
    'Jason',
    'Danielle',
    'Mom',
    'Dad',
    'Suzy',
    'Dale',
    'Aly',
    'Chris'
]

numbers = list(range(1, len(names) + 1))
random.shuffle(names)

assignments = dict(zip(names, numbers))
assignments = OrderedDict(sorted(assignments.items(), key=lambda t: t[1]))

tree = '''
      /\      
     /\*\     
    /\O\*\    
   /*/\/\/\   
  /\O\/\*\/\  
 /\*\/\*\/\/\ 
/\O\/\/*/\/O/\
      ||      
      ||      
      ||'''


print(tree)
print()
print() 
print('Order')
print('-------------------')
for name, number in assignments.items():
    print(number, '----->', name)


print()
print()
print('Gifts')
print('-------------------')

fun = list(string.ascii_lowercase)
fun = fun[:len(assignments)]
random.shuffle(fun)
count = 0
for name in assignments.items():
    print(f"{fun[count]} ------> {name}")
    count += 1

# random.shuffle(names)

# gifts = dict(zip(names, numbers))
# print(gifts)
# for name, number in gifts.items():
#     print(name, '----->', number)

used_numbers = []

# count = 1
# # for name, num in assignments.items():
# while 1:
#     try:
#         print()
#         print(f"Number {count} is up!")
#         # print(f"{name} is up!")
#         gift_number = int(input('To pick a gift: enter a random number between 1 and {} inclusive:  '.format(len(names))))
#         if gift_number in used_numbers:
#             print('That number has already been selected.  Try again!')
#         # elif gift_number == count:
#         #     print('That is your number.  Try again!')
#         else:
#             count += 1
#         print("You selected {}\'s gift!".format(names[gift_number - 1]))
#         used_numbers.append(gift_number)
#     except KeyboardInterrupt:
#         import sys
#         sys.exit()
#     except:
#         pass
