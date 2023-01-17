#import random
#cowlist = ["how", "now", "brown", "cow"]
#random.shuffle(cowlist)

#print(cowlist)

#############################################

#user input string of words 
#join array of words, //.join(words)
#rearrange with random.shuffle
#print

#############################################

import random 

def rearrange_words(list_of_words):
  random.shuffle(list_of_words)
  result = ' '.join(words)
  print(result)

if __name__ == '__main__':
  words = input(str("Enter 4 words: ")).split()
  rearrange_words(words)

