from nltk import word_tokenize
input_words = "I want to buy a new phone"

word_tokenized=word_tokenize(input_words)

from nltk.corpus import stopwords

stopWords=set(stopwords.words('english'))

words_filtered=[]

for w in word_tokenized:
    if w not in stopWords:
        words_filtered.append(w)

print("Stop Words Filtered Sentence", words_filtered)

from nltk.stem import PorterStemmer

ps=PorterStemmer()

stemmed=[]

for word in words_filtered:
    stemmed.append((word))

print("Stemmed Words: ",stemmed)

import nltk

noun = []
noun_filtered=[]
for sent in stemmed:
    noun = noun + nltk.pos_tag(nltk.word_tokenize(sent))

for word in noun:
    if 'NN'  in word:
       noun_filtered.append(word)
    if 'FW' in word:
        noun_filtered.append(word)
    if 'SYM' in word:
        noun_filtered.append(word)
noun_filtered_twice=[]
total=len(noun_filtered)
for i in range(total):
    noun_filtered_twice.append(noun_filtered[i][0])

print(noun_filtered_twice)

from nltk.corpus import wordnet


#####wordnet using ########

synonyms = []
antonyms = []

for syn in wordnet.synsets("phone"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(syn)

