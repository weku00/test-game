# rock paper scissors fuck
#_________________________________

#import
# yfrom multiprocessing import RLock
import time
import random 

# loop for game
while True:

  #opening 
  print('Rock Paper Scissors!') 

  # varibles, name, player picked option
  # player = input('Whats your name? ')
  p_op = input('what do you pick? ')
  countdown = range(1,4)
  options = ['rock', 'paper', 'scissors']

  # computer picks a random choice from options
  c_op = random.choice(options)
  
  # countdown from 1 to 3
  for count in countdown:
        print(count)
        time.sleep(1)
        
  #weird style line ig  
  print('''Computer               Player''')

  # tells who wins or looses 
  def game_logic():
    if p_op == c_op:
      print(c_op + '| Draw! |' + p_op)
    # rock beats scissors
    elif p_op == options[1]:
        if c_op == options[-1] :
          print(c_op + ' |Rock wins! |'+ p_op)
      # scissos beats paper
    elif p_op == options[-1]:
        if c_op == options[2]:
          print(c_op + ' | Scissors wins! |'+ p_op)            
      #paper beats rock
    elif p_op == options[2]:
      if c_op == options[1]:
          print(c_op + '| Paper wins! |' + p_op)
    elif p_op != options:
          print('error, pick from ' + str(options))

  # calling game 
  game_logic()
  
  # loop for game
  play_again = input('Play again (y, n)')
  if play_again.lower() != 'y':
    break
