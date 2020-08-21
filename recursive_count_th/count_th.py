'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    #Base case if word is 0 characters or 1 character return 0
    if len(word) < 2:
        return 0

    #Check if first two characters are equal --> recursively call to increment along 'word' one character at a time
    # add 1 for each occurance of 'th'
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])