from random import randint


def divisibleby(n):
      if n % 2 == 0:
            return 'divisible by 2'
      elif n % 3 == 0:
            return 'divisible by 3'
      else:
            pass


# generate a random number
random_number = randint(1, 10)

loop = True
while(loop):
      hint = []
      try:
        # get user guess
        print('')
        guess = int(input('enter your guess number: '))
        print('')

        # check if correct and give a hint
        if guess == random_number:
              print('correct!')
              loop = False
              
        elif guess < random_number:
              hint.append('higher')
              hint.append(divisibleby(random_number))
            
              for h in hint:
                    print(h)
        else:
              hint.append('lower')
              hint.append(divisibleby(random_number))
              
              for h in hint:
                    print(h)
                
      except ValueError:
        print('only number is allowed')
        
  
    

  