import nltk
import random as rd #to make random decisions



def NN(): #find nouns
    lNN = []
    for i in tags:
        if 'NN' in i:
            lNN.append(i[0])
    return lNN



with open(r'C:\Users\admin2\desktop\madlib\text.txt', 'r') as text:
    tok_text = nltk.word_tokenize(text.read()) #tokenization
    tags = nltk.pos_tag(tok_text) #tagging
    new_items = [i if i not in NN() else 'TEST' for i in tok_text] #replace word
    print(new_items)

""" To Do:
1. Find other parts of speech
2. Make a list for each part of speech
3. Make a function to randomly choose from said lists
4. Think of a way to randomly select words to replace """
