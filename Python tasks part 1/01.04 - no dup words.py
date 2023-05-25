'''
Create a function that takes a sentence and prints the sentence without duplicated words
'''
def no_dup_words1(x):
    return ' '.join(set(x.split()))

def no_dup_words2(x):
    return ' '.join(dict.fromkeys(x.split()))

def no_dup_words3 (x):
    words = x.split()
    return ' '.join(sorted(set(words),key = words.index))


    
