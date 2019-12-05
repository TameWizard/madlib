import nltk
import random as rd  # to make random decisions


def fNN():  # find nouns
    lNN = []
    for i in tags:
        if 'NN' in i:
            lNN.append(i[0])
    return lNN

def nNN():
    lNN = ['TEST1', 'TEST2', 'TEST3', 'TEST4']
    numNN = rd.randrange(0, len(lNN))
    res = lNN[numNN]
    return(res)

with open(r'C:\Users\admin2\desktop\madlib\text.txt', 'r') as text:
    tok_text = nltk.word_tokenize(text.read())  # tokenization
    tags = nltk.pos_tag(tok_text)  # tagging
    new_items = [i if i not in fNN() else nNN() for i in tok_text]  # replace word

def make_text(text):
    punct = ['!', '.', ',', '?', ':', ';']
    res = ''
    for i in text:
        if i not in punct:
            res = res + ' '  + i
        else:
            res = res + i
    return res

print(make_text(new_items))


""" To Do:
1. Find other parts of the speech
2. Make a list for each part of the speech
3. Make a function to randomly choose from the said lists - Done
4. Think of a way to randomly select words to replace """
