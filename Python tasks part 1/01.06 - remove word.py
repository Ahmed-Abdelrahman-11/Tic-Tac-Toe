'''
Create a function that takes a sentence and word and remove the word from the sentence
'''
def remove_word(x,y):
    words = x.split()
    words.remove(y)
    return ' '.join(words)
