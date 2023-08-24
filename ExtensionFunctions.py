
sign = "======================================\nWelcome to Learn English with Python\n======================================"    
instructions = ">>> write 'n' for unknowing the answer, 'q' for quit the program <<<" 
white_space = '------------------------------------------------------'


 
def memorized(score):
    if score == 1:
        print(f'you memorized {score} word, correct answer!')
        print(white_space)
    else:
        print(f'you memorized {score} words, correct answer!')
        print(white_space)

def info():
    from MainFile import ar_word
    print(f'the answer is : ({ar_word})')
    print(white_space)
    
# this func will work soon
# def correct_answer(current_line):
#     with open('SavedWords.txt', 'a', encoding='utf-8') as SaveFile:
#         SaveFile.write(current_line)
    
#     total =''    
#     with open('English Words/Words.txt' ,'r' ,encoding='utf-8') as file:
#         words = file.read().splitlines()
    
#     for line in words :
#         if line != current_line:
#             total += line + '\n'
            
#     with open('English Words/Words.txt' ,'w' ,encoding='utf-8') as myfile:
#         myfile.write(total)
    


def result(score):
    if score == 10:
        print('great job! you memorized 10 words')
        input('\nthe program is finished with 0')
        exit()
    elif score >= 6 :
        print(f'you do will , try harder again ,your memorized words "{score}"')
        input('\nthe program is finished with 0')
        exit()
    else:
        print('you should have a review on vocabulary ,and try again')
        input('\nthe program is finished with 0')
        exit()