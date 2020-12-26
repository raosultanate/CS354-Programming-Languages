
from collections import Counter
import operator
import string
import sys

# grabs argument
filename = sys.argv[1]

#function get rids of punctuation and casts to lower also makes counts
def fileReader(fname):
    with open(fname) as f:
        content = f.read()
        string_no_punc = content.translate(str.maketrans('', '', string.punctuation))
        lowerCaseString = string_no_punc.lower()
        return Counter(lowerCaseString.split())
        
#function call of above.
counter = fileReader(filename)

#sorts the result in descending order of the counts
sorted_counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

#print out the result to the screen. (converts the list to the string)
str0 = '\n'.join(map(str, sorted_counter)).translate(str.maketrans('', '', string.punctuation))
print(str0)

#usage: python3 wf.py Gettysburg-Address.txt

