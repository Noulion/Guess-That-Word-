#Guess. that .word!

"""
@Noulion in github!

A small indie game. Goal is to guess the word given by the other player!.

To play, you must execute and not show the code.

I'm soon making a internal input data for the word and hint, So that it wont be a hassle always changing the string after every game, But it is what it is for now.

If you manage to turn this into that, make sure to fork it so i would know your work!^.^
"""

import time
from termcolor import colored

#Title_bar RGB style

title = [(colored("GUESS. ", 'light_red')+(colored("THAT. ", 'green')+(colored("WORD!.", 'cyan'))))]

for i in title:
    j = ""
    print(i, '\n\n')


#Word to guess (Fill one up[The default one is for an example])

#change after a round
word = "Hello"
wordL = len(word)
wordL = " __ " * wordL
wordL2 = len(word)
hint_text = "-" #change this hint to match the word.

print(colored('hints:', 'white')+(colored(hint_text, 'white', 'on_green', ['bold'])))
print(colored(f" [{wordL}] ({wordL2}) letter word", 'white'), '\n')

#indicator variable to word as guess.
guess = word 

#tell the player if ready.
start_guessing = input(colored('Press Enter To GUESS! [»]', 'white'))
print(start_guessing, end="\n")

if start_guessing == start_guessing:
     None

#Where the fun begins.
while guess:
    print(colored("  [Give Up?, type g]", 'white'))
    
    try_i = input(colored("  Guess the word!: ", 'white'))
    
    if try_i == word: #win.
        time.sleep(0.6) #Time is here so it gives an edging feeling, same even with wrong guesses
        print(colored(f"\n  You guessed '{word}', correct!\n", 'cyan'))
        break
        
    elif try_i == 'g':
        print(colored(f"\n  The word was {word}\n", 'magenta')) 
        break
    
    elif try_i == '': #The given input is blank.
        print('\n  Blank isnt a word.\n')
    
    else: #Any guess that is a word and WRONG will be on this. 
        bad_words = ['nigger', 'fucker', 'shit']
      
        if try_i == bad_words[1]:
            print(colored(f"\n{s:6}NO RACIST, '{try_i}' is definitely wrong!!\n", 'light_red'))
            break
            
        time.sleep(0.6)  
        s = "" #Had problems using spacer on text.#
        print(colored(f"\n{s:6}Try Again!, '{try_i}' is wrong!!\n", 'light_red'))
