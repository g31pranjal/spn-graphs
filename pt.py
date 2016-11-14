import nltk
from nltk.parse.stanford import StanfordDependencyParser
from nltk.parse.stanford import StanfordParser

path_to_jar = 'stanford-parser/stanford-parser-full/stanford-parser.jar'
path_to_models_jar = 'stanford-parser/stanford-parser-full/stanford-parser-3.5.2-models.jar'

parser = StanfordParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

result = parser.raw_parse("My seeing with the telescope caused him to die")


lst = list(result)[0]

print lst