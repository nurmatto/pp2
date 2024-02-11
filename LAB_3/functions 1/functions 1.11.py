word=input()
def reverser(word):
    new_word=word[::-1]
    if word==new_word:
        print('Yeah, this one is palindrome')
    else:
        print('Sorry, maybe next time :)')
        
reverser(word)
