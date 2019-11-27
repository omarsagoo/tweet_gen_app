import random
import sys

# Create reverse() func to reverse a list.
# ' '.join the list to return it back to a sentence. and have functionality to turn a string into a list
#
def reverse(params):
    #
    # Check a list to see if it has more than one item,
    # If not turn the string word into a list and pass the argument back in through recursion.
    #
    if len(params) != 1:
        # Store the last index in index_end variable
        #
        index_end = len(params) - 1
        #
        # iterate through a range of half the index rounded down
        #
        for i in range(round(index_end/2)):
            # swap the first and last index then increment/ decrement respectively
            #
            params[i], params[index_end] = params[index_end], params[i]
            i += 1
            index_end -= 1
        params = " ".join(params)
        return params
    else:
        # if only one item in the list, grab the item turn it into a string, then turn it back into a list
        # pass the variable back into the function recursively
        #
        params = str(params[0])
        params = list(params)
        return reverse(params)



if __name__ == "__main__":
    params = sys.argv[1:]
    print(reverse(params))
    