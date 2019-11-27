from sys import argv
from rearrange import input_handler

'''ART taken from online, did not make this myself'''


def cowsay(prompt):
    '''function that formats a defined string dynamically'''

    Cow = '''
   {}
   ^__^                             
   (oo)\_______                   
   (__)\       )\/\             
       ||----w |           
       ||     ||  
       
       '''

    return Cow.format(prompt)

if __name__ == "__main__":
    print(cowsay(input_handler("what do you want the cow to say? ")))