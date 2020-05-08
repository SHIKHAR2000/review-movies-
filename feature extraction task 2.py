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
>>> all_words = [word.lower() for word in movie_reviews.words()]

 
>>> print (all_words[:10])
['plot', ':', 'two', 'teen', 'couples', 'go', 'to', 'a', 'church', 'party']
>>> from nltk import FreqDist
>>> all_words_frequency = FreqDist(all_words)

>>> print (all_words_frequency)
<FreqDist with 39768 samples and 1583820 outcomes>
>>> print (all_words_frequency.most_common(10))
[(',', 77717), ('the', 76529), ('.', 65876), ('a', 38106), ('and', 35576), ('of', 34123), ('to', 31937), ("'", 30585), ('is', 25195), ('in', 21822)]
>>> 