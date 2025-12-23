
a= """OMG!!! I luv NLP <3. It's sooooo coool! #AI #MachineLearning.
BTW, NLP isn't easy at all... but it's FUN!!! 😄😄
In college, students read blogs, tweets, research papers, emails, and chat messages daily!!!
Some texts are clean; others are FULL of typos, slangggg, emojis 😂😂, and random CAPS.
In 2025, AI-powered systems process MILLIONS of documents @ scale—fast & continuously.
If your data isn't clean and normalized properly, your model WILL fail badly!!! 💥💥
Trust me: garbage in = garbage out."""
#Normalisation
a=a.lower()


#Handling Contractions
import contractions
expand=contractions.fix(a)
a=expand


#Noise Removal
for char in a:
    if char.isalnum()==0:
        a=a.replace(char," ")


#Tokenisation
token=a.split()
print("token\n",token)


#Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmas=[lemmatizer.lemmatize(x) for x in token]
print("lemmas\n",lemmas)


#spell check as it's written in slang 
from spellchecker import SpellChecker
spell=SpellChecker()
newwords=["ai","nlp","emojis","machinelearning","omg"]
finaltokens=[]
for words in lemmas:
    if words in newwords:
        finaltokens.append(words)
    else:
        finaltokens.append(spell.correction(words))
print("finaltokens\n",finaltokens)


#removal of stopwords
from nltk.corpus import stopwords
stop_word=set(stopwords.words("english"))
l=[]
for x in finaltokens:
    if x not in stop_word:
        l.append(x)
print("Removal of stopwords\n",l)


#Vectorisation Preview
d={}
for vector in l:
    if vector not in d:
        d[vector]=0
    d[vector]+=1
print("Vectorised Preview\n",d)
