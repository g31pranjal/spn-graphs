import nltk
from nltk.parse.stanford import StanfordDependencyParser
from nltk.parse.stanford import StanfordParser
import np_parser
import vp_parser


path_to_jar = 'stanford-parser/stanford-parser-full/stanford-parser.jar'
path_to_models_jar = 'stanford-parser/stanford-parser-full/stanford-parser-3.5.2-models.jar'

parser = StanfordParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)


knowledgeBase = []


def prnt() :
	for kw in knowledgeBase :
		print kw 	


def addToKB(sentence) :

	result = parser.raw_parse(sentence)
	lst = list(result)[0]

	np = np_parser.getNP(lst)
	for entry in np :
		if entry['noun'] is None :
			np.remove(entry)

	vp = vp_parser.getVP(lst)

	for nps in np :
		for vps in vp :
			tup = (nps, vps)
			knowledgeBase.append(tup)

		
def query(tokens) :
	a1 = set(queryAP(tokens[0]))
	a2 = set(queryAction(tokens[1]))
	a3 = set(queryAP(tokens[2]))

	a = list(a1.intersection(a2.intersection(a3)))

	for el in a :
		print(" > " + prettify(knowledgeBase[el]))


def queryAP(tk) :
	if tk is '?' :
		t = []
		for i in range(0, len(knowledgeBase)) :
			t.append(i)
		return t
	else :
		t = []
		for i in range(0, len(knowledgeBase)) :
			m = knowledgeBase[i][1]['np']
			if (knowledgeBase[i][0]['noun'] == tk) or (m['noun'] == tk) :
				t.append(i)
		return t
	

def queryAction(tk) :
	if tk is '?' :
		t = []
		for i in range(0, len(knowledgeBase)) :
			t.append(i)
		return t
	else :
		t = []
		for i in range(0, len(knowledgeBase)) :
			if knowledgeBase[i][1]['main'] == tk :
				t.append(i)

		return t


def prettify(tup) :

	np = tup[0]
	vp = tup[1]

	np_p = ""

	if np['det'] is not None :
		np_p = np['det'] +  " "

	if np['adj'] is not None :
		np_p = np_p + np['adj'] +  " "

	np_p = np_p + np['noun'] + " "

	if np['prep'] is not None :
		np_p = np_p + np['prep'] +  " "

	vp_p = ""

	npvp = vp['np']

	vp_p = vp['main'] + " "

	if npvp['det'] is not None :
		vp_p = vp_p + npvp['det'] +  " "

	if npvp['adj'] is not None :
		vp_p = vp_p + npvp['adj'] +  " "

	vp_p = vp_p + npvp['noun'] + " "

	if npvp['prep'] is not None :
		vp_p = vp_p + npvp['prep'] +  " "

	if vp['adverb'] is not None :
		vp_p = vp_p + vp['adverb']

	return np_p + " " + vp_p






