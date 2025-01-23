import random
input_number = input("Lets play Stone Paper Scissors \n Type either stone,paper or scissor --->")
paper = '''
        ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
'''
stone = '''
        ,--.--._    
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
  '''
scissor = '''

   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
  '''

choices = [paper, stone, scissor]
random_integer = random.choice(choices)

if input_number == random_integer:
    print(random_integer, "\n ITS A DRAW!")
elif (random_integer == scissor and input_number == "paper") or \
        (random_integer == stone and input_number == "scissor") or \
        (random_integer == paper and input_number == "stone"):
    print(random_integer, "\n YOU LOST")
else:
    print(random_integer, "\n YOU WON!!!")