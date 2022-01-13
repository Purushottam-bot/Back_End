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

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...sdd..sddddd...dsssss...sdddd'
test_patterns =['sd{1,3}']
multi_re_find(test_patterns,test_phrase)
