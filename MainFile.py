from ExtensionFunctions import *

print(sign)
print(instructions)


score = 0

with open("Words.txt" ,encoding='utf-8') as file :
        show = file.read().splitlines() 
for n in range(10):
  word = show[n].split(maxsplit=1)
  en_word = word[1]
  ar_word = word[0]
  answer = ""
  while answer != ar_word :
    answer = input(f"what is the meaning of ({en_word}) in Arabic : ")  
    if answer == ar_word :
      score += 1 
      memorized(score)
      # correct_answer(word) # this func will work soon
    elif answer == 'n' :
      print(f'the answer is : ({ar_word})')
      print(white_space)
      break
    elif answer == 'q' :
      input('\nthe program is finished with 0')
      exit()
    else:
      print('Wrong Word, try again!') 
result(score)  

          


      