import nltk
import random as rd  # to make random decisions

def nNN():
    NN = ['TEST1', 'TEST2', 'TEST3', 'TEST4']
    num = rd.randrange(0, len(NN))
    res = NN[num]
    return(res)
    
def nVB():
    VB = ['Test1', 'Test2', 'Test3', 'Test4']
    num = rd.randrange(0, len(VB))
    res = VB[num]
    return(res)
    
def make_new_items(tok_text):
    new_items = []
    for i in tok_text:
        if i in lNN:
            new_items.append(nNN())
        elif i in lVB:
            new_items.append(nVB())
        else:
            new_items.append(i)
    return new_items

with open(r'C:\Users\admin2\desktop\madlib\text.txt', 'r') as text:
    tok_text = nltk.word_tokenize(text.read())  # tokenization
    tags = nltk.pos_tag(tok_text)  # tagging
    lVB = [i[0] for i in tags if 'VBD' in i] # find verbs
    lNN = [i[0] for i in tags if 'NN' in i] # find nouns
    almost_ready = make_new_items(tok_text)  # replace words

def make_text(text):  # unite the string 
    punct = ['!', '.', ',', '?', ':', ';']
    res = ''
    for i in text:
        if i not in punct:
            res = res + ' '  + i
        else:
            res = res + i
    return res[1:]

print(make_text(almost_ready))


""" To Do:
1. Find other parts of the speech - Done
2. Make a list for each part of the speech - Done
3. Make a function to randomly choose from the said lists - Done
4. Think of a way to randomly select words to replace """
