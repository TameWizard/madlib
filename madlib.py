import nltk
import random as rd

NN = []
fNN = open('dicNN.txt', 'r')
for i in fNN:
    NN.append(i.replace('\n', ''))
fNN.close()

VB = []
fVB = open('dicVB.txt', 'r')
for i in fVB:
    VB.append(i.replace('\n', ''))
fVB.close()

JJ = []
fJJ = open('dicJJ.txt', 'r')
for i in fJJ:
    JJ.append(i.replace('\n', ''))
fJJ.close()

def ser(tag):
    num = rd.randrange(0, len(tag))
    res = tag[num]
    return(res)
    
def make_new_items(tok_text):
    new_items = []
    for i in tok_text:
        if i in lNN:
            if i.isupper() == True:
                new_items.append(ser(NN).capitalize())
            else:
                new_items.append(ser(NN))
        elif i in lVB:
            if i.isupper() == True:
                new_items.append(ser(VB).capitalize())
            else:
                new_items.append(ser(VB))
        elif i in lJJ:
            if i.isupper() == True:
                new_items.append(ser(JJ).capitalize())
            else:
                new_items.append(ser(JJ))
        else:
            new_items.append(i)
    return new_items

with open(r'full_text.txt', 'r') as text:
    tok_text = nltk.word_tokenize(text.read())  # tokenization
    tags = nltk.pos_tag(tok_text)  # tagging
    lVB = [i[0] for i in tags if 'VBD' in i] # find verbs
    lNN = [i[0] for i in tags if 'NN' in i] # find nouns
    lJJ = [i[0] for i in tags if 'JJ' in i] # find adj
    almost_ready = make_new_items(tok_text)  # replace words

def make_text(text):  # unite the string 
    stop = ['!', '.', ',', '?', ':', ';', "n't", "'m", "'s", "'", "'re"]
    res = ''
    for i in text:
        if i not in stop:
            res = res + ' '  + i
        else:
            res = res + i
    return res[1:]

print(make_text(almost_ready))
