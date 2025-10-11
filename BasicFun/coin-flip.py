#Flipping a coin results a head or a tail with 1/2 probability

import random

num = random.randint(0, 1)
             
if num > 0.5: 
  print('Heads')
else:
  print('Tails')  
