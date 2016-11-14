from nltk.tree import Tree
import np_parser



def getVP(root) :

	if str(root.label()) != "ROOT" :
		return list()

	else :
		# print root

		rootLength = root.height()
		sentence = root[0]

		return VPExtract(sentence[1])


def VPExtract(verbTree) :
	# print "go fast !"
	# print verbTree

	labels = [ str(verbTree[i].label()) for i in range(0, len(verbTree)) ]

	# case of 'VP' and 'VP'
	if 'CC' in labels and 'VP' in labels :
		return [ VPExtract(verbTree[i]) for i in range(0, len(verbTree)) if str(verbTree[i].label()) == 'VP' ]
	
	# case of VB_ VP
	elif 'NP' not in labels and 'S' not in labels :
		add = " ".join(verbTree[0].leaves())
		inc = VPExtract(verbTree[1])
		for entry in inc :
			entry['main'] = add + " " + entry['main']
			return inc

	# case of VB_ NP []
	else :
		lst = []
		
		dct = {}
		dct['main'] = " ".join(verbTree[0].leaves())
		# dealing with patient NP
		if len(verbTree) == 3 :
			dct['adverb'] = " ".join(verbTree[2].leaves())
		else :
			dct['adverb'] = None;

		nps = np_parser.NPExtract(verbTree[1])
		for entry in nps :
			tmp = {}
			if entry['noun'] is not None :
				tmp['main'] = dct['main']
				tmp['adverb'] = dct['adverb']
				tmp['np'] = entry
				lst.append(tmp)

				
		
		return lst
		# if nps is a list with more the 1 element, copy dct to more elements in the list


