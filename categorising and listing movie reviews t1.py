Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from nltk.corpus import movie_reviews
>>> print (len(movie_reviews.fileids()))
2000
>>> print (movie_reviews.categories())
['neg', 'pos']
>>> print (len(movie_reviews.fileids('pos')))
1000
>>> print (len(movie_reviews.fileids('neg')))
1000
>>> positive_review_file = movie_reviews.fileids('pos')[0]
>>> print (positive_review_file)
pos/cv000_29590.txt
>>> documents = []
>>> for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.append((movie_reviews.words(fileid), category))

		
>>> print (len(documents))
2000
>>> print (documents[0])
(['plot', ':', 'two', 'teen', 'couples', 'go', 'to', ...], 'neg')
>>> from random import shuffle
>>> shuffle(documents)
>>> 