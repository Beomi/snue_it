import re
import collections

def check_dup():
    f = open('imgo.txt', 'r')  # Google Spread Sheet download with tsv, save as with txt(same contents)
    txt = f.read()
    rule = re.compile('\d{8}') # Get elements consist of 8 digit numbers
    result = rule.search(txt)
    
    counter = collections.Counter(result)
    
    return counter
    
if __name__=='__main__':
    counter = check_dup()
    print(counter)
