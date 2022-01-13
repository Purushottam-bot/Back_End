import inside
import re

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print ('Searching the phrase using the re check: {}'.format(pattern))
        print (re.findall(pattern,phrase))
        print ('\n')

test_phrase = 'This is a string! BBSBut it has punctuation. How can we remove it?'
test_patterns =['[A-Z][a-z]+']
multi_re_find(test_patterns,test_phrase)

inside.func()
