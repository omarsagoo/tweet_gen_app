import random
import sys
from itertools import permutations 



# fisher-Yates Shuffle Method
def randomizer(params):

    # store the length of the list in a variable called i
    i = len(params)

    # while loop that checks to see if i becomes less than 1.
    # less than one appropriately means that it has gone through the entire list
    while i > 1:
        # Decrements i by 1
        i -= 1 

        # create a variable j that stores a random integer between 0 and i
        j = random.randint(0,i)

        # swaps the list items with index i and j
        params[i], params[j] = params[j], params[i]

    return params
        

# function that creates an anagram out of a given word. uses the same logic as the fisher-yates shuffle method in the randomizer function
def anagramizer(s):
    return set([''.join(perm) for perm in permutations(s)])



    

# Handles improper user input
def input_handler(prompt):
    user_input = input(prompt)
    # checks if the user didnt put any words or characters
    if user_input == '':
        return input_handler("you must enter a word! ")

    # checks if the word is only white space
    elif user_input.isspace():
        return input_handler("you must enter a word! ") 

    # returns the user input with the white space on the beginning and the end removed
    return user_input.strip()





if __name__ == "__main__":
    params = sys.argv[1:]

    print(randomizer(params)) 
    print(anagramizer(input_handler('What word would you like an anagram for? ')))
    # perms = (p for p in permutations('hello'))
    # for p in perms:
    #     print(''.join(p))

    