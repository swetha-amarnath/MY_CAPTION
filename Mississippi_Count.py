#Functions
#Enter a string - Mississippi

abc= input('Please enter a string: ')
def most_frequent(string):
    d = dict()
    for letters in string:
        if letters not in d:
            d[letters] = 1
        else:
            d[letters] += 1
    for w in sorted(d, key=d.get, reverse=True):
        print(w,':',d[w])

print (most_frequent(abc))