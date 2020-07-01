# String  is split into  equal parts of length . 
# We convert each  to  by removing any subsequent occurrences non-distinct characters
# We then print each on a new line.


import textwrap
from collections import OrderedDict


def merge_the_tools(string, k):
    if len(string) >=1 and len(string)<=10000:
        if k>=1 and k<=len(string):
            
            list_of = textwrap.wrap(string, k)
            for elem in list_of:
                print("".join(OrderedDict.fromkeys(elem)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
