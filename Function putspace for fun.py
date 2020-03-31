def putspace(string):
    global newstring
    newstring = ''
    for i in string:
        newstring += i
        if i == ',':
            newstring += ' '
    return newstring

### STRING MUST HAVE COMMAS THAT INDICATE WHERE SPACES GO
### TO IMPROVE CODE: Convert string to list, use index + 1 to predict if next number also number

spaced = putspace('5,13,30,34,36,38,40,46,56,58,62,63,65,68,90')

print(spaced)

