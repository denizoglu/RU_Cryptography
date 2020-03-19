#!/usr/bin/python3

from string import ascii_lowercase

def get_frequencies(file):
    '''
    Reads the 'file' and returns dictionary 'dic'
    '''
    with open(file) as f:
        text = f.read().strip()
        dic = {}
        for x in ascii_lowercase:
            dic[x] = text.count(x)
    return dic

if __name__ == "__main__":
    file = 'encoded_sample.txt'
    dic = get_frequencies(file)
    print(dic)