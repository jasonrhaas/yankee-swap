import random


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

random.shuffle(names)

# gifts = dict(zip(names, numbers))
# print(gifts)
# for name, number in gifts.items():
#     print(name, '----->', number)

used_numbers = []

count = 1
while 1:
    try:
        print()
        print(f"Number {count} is up!")
        gift_number = int(input('Enter a random number between 1 and {} inclusive:  '.format(len(names))))
        print("You selected {}\'s gift!".format(names[gift_number - 1]))
        if gift_number in used_numbers:
            print('That number has already been selected.  Try again!')
        else:
            count += 1
        used_numbers.append(gift_number)
    except KeyboardInterrupt:
        import sys
        sys.exit()
    except:
        pass
