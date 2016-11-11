import nltk 

def tag(data) :
	tkns = nltk.word_tokenize(data)
	tagged = nltk.pos_tag(tkns)

	print tagged
