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
>>> from nltk.corpus import stopwords
>>> stopwords_english = stopwords.words('english')
>>> print (stopwords_english)
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
>>> all_words_without_stopwords = [word for word in all_words if word not in stopwords_english]

>>> print (all_words_without_stopwords[:10])
['plot', ':', 'two', 'teen', 'couples', 'go', 'church', 'party', ',', 'drink']
>>> all_words_without_stopwords = []
>>> for word in all_words:
	    if word not in stopwords_english:
		       all_words_without_stopwords.append(word)

		       
>>> print (all_words_without_stopwords[:10])
['plot', ':', 'two', 'teen', 'couples', 'go', 'church', 'party', ',', 'drink']
>>> import string
>>> print (string.punctuation)
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
>>> all_words_without_punctuation = [word for word in all_words if word not in string.punctuation]
>>> print (all_words_without_punctuation[:10])
['plot', 'two', 'teen', 'couples', 'go', 'to', 'a', 'church', 'party', 'drink']
>>> all_words_clean = []
>>> for word in all_words:
	 if word not in stopwords_english and word not in string.punctuation:
		 all_words_clean.append(word)

		 
>>> print (all_words_clean[:10])
['plot', 'two', 'teen', 'couples', 'go', 'church', 'party', 'drink', 'drive', 'get']
>>> all_words_frequency = FreqDist(all_words_clean)
>>> print (all_words_frequency)
<FreqDist with 39586 samples and 710578 outcomes>
>>> print (all_words_frequency.most_common(10))
[('film', 9517), ('one', 5852), ('movie', 5771), ('like', 3690), ('even', 2565), ('good', 2411), ('time', 2411), ('story', 2169), ('would', 2109), ('much', 2049)]
>>> print (len(all_words_frequency))
39586
>>> most_common_words = all_words_frequency.most_common(2000)
>>> print (most_common_words[:10])
[('film', 9517), ('one', 5852), ('movie', 5771), ('like', 3690), ('even', 2565), ('good', 2411), ('time', 2411), ('story', 2169), ('would', 2109), ('much', 2049)]
>>> print (most_common_words[1990:])
[('remain', 64), ('anna', 64), ('moved', 64), ('asking', 64), ('genuinely', 64), ('rain', 64), ('path', 64), ('aware', 64), ('causes', 64), ('international', 64)]
>>> word_features = [item[0] for item in most_common_words]
>>> print (word_features[:10])
['film', 'one', 'movie', 'like', 'even', 'good', 'time', 'story', 'would', 'much']
>>> def document_features(document):
	 document_words = set(document)
	  features = {}
	  
SyntaxError: unexpected indent
>>> def document_features(document):
	 document_words = set(document)
	 features = {}
	 for word in word_features:
		 features['contains(%s)' % word] = (word in document_words)
		 return features

		
>>> movie_review_file = movie_reviews.fileids('neg')[0]
>>> print (movie_review_file)
neg/cv000_29416.txt
>>> print (documents[0])
(['anna', 'and', 'the', 'king', 'strides', 'onto', ...], 'pos')
>>> feature_set = [(document_features(doc), category) for (doc, category) in documents]
>>> print (feature_set[0])
({'contains(film)': True}, 'pos')
>>> feature_set = []
>>> for (doc, category) in documents:
	feature_set.append((document_features(doc), category))

	
>>> print (feature_set[0])
({'contains(film)': True}, 'pos')
>>> print (len(feature_set))
2000
>>> test_set = feature_set[:400]
>>> train_set = feature_set[400:]
>>> print (len(train_set))
1600
>>> print (len(test_set))
400
>>> from nltk import NaiveBayesClassifier
>>> classifier = NaiveBayesClassifier.train(train_set)
>>> 