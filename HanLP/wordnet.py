#! python3
# coding=gbk

# import nltk
# nltk.download('wordnet')

from nltk.corpus import wordnet as wn

print(wn.synsets('published'))
dog = wn.synset('dog.n.01')
print(dog.hypernyms())
print(dog.hyponyms())
