import nltk
from nltk.parse.stanford import StanfordDependencyParser
from nltk.parse.stanford import StanfordParser

path_to_jar = 'stanford-parser/stanford-parser-full/stanford-parser.jar'
path_to_models_jar = 'stanford-parser/stanford-parser-full/stanford-parser-3.5.2-models.jar'

parser = StanfordParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

result = parser.raw_parse("I saw Tom with the telescope")


print list(result)


# while r is not None  :
# 	print "--> " + str(r)
# 	r = result.next()