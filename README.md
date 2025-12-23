Week 1:
Write a Python script to clean this dirty paragraph:

> OMG!!! I luv NLP <3. It's sooooo coool! #AI #MachineLearning.
BTW, NLP isn't easy at all... but it's FUN!!! 😄😄
In college, students read blogs, tweets, research papers, emails, and chat messages daily!!!
Some texts are clean; others are FULL of typos, slangggg, emojis 😂😂, and random CAPS.
In 2025, AI-powered systems process MILLIONS of documents @ scale—fast & continuously.
If your data isn't clean and normalized properly, your model WILL fail badly!!! 💥💥
Trust me: garbage in = garbage out.

Steps:
1. Normalisation: using str.lower()
2. Handling contraction(extra step): using contractions library and expanding words like isn't to is not, btw to by the way, it's to it is.
3. Noise Removal: replacing special characters !,<, etc with space
4. Tokenisation: using str.split(), it gives a list of words
5. Lemmatization: using nltk library, using WordNetLemmatizer, it converts words to their roots while preserving its meaning unlike stemming. But it didn't convert powered to power, normalized to normalize.
   Moreover, it changed "caps" to cap which is a thing to wear but according to the paragraph it means capital letters, thus it changes its meaning.
7. Spell Check(extra step): Using spellchecker library (spell.correction()). But, it converts words like-
   "nlp" to nap,
   "omg" to om,
   "machinelearning" to None,
   "sooooo" to vodoo,
   "slanggg" to slanging,
   "emojis" to emesis.
   Thus, we created a list of words that have meaning and are prone to change by the function spell.correction(). we did the correction if the word didn't belong to the list of new words.
8. Removal of stopwords: Using nltk library, using stopwords corpus #comment: in today's context: words like omg, btw, lol can be treated as stopwords.
9. Vectorisation Preview: Making a dictionary with words as keys and their frequency as values.
   
Problems:
1. "soooo" is still written as "vodoo" and "slanggg" as "slanging". It can be done manually.
2. we were able to remove special characters but didn't remove numbers, in "<3", we didn't remove 3 and it doesn't make any sense. If we remove all the numbers, then "2025" with makes sense and adds meaning to
   the paragraph will also be removed.
3. words like "not" are also removed from the corpus as they are stopwords but it destroys meaning of the paragraph.
