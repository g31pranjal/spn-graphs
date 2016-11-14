from nltk.tree import Tree
import vp_parser



def getNP(root):
	lost =[]
	if root is None:
		return list()
	else:
		s_phrase = root[0]
		np_phrase = s_phrase[0]			
		lost = NPExtract(np_phrase)
		
	return lost

def NPExtract(var):

	pronoun = ["PRP","POS", "PRPS"]
	proper_noun = ["NNP", "NNPS","NNS","NN"]
	adjective = ["JJ","JJS","JJR","ADJP"]

	data = [{}, {}]
	j=0
	for j in range(0,2):
		
		data[j] = {'noun': None , 'adj':None,  'det':None, 'prep':None}

	def cc_absent(temp):
		i=0
		# print temp.height()
		# print temp
		if temp.height() > 2:
			for i in range(0,len(temp)):				
				if (temp[i].label() in  pronoun):
					stri = str(" ".join(temp[i].leaves()))
					data[0]['noun'] = (stri)
				if temp[i].label() in proper_noun:
					stri = str(" ".join(temp[i].leaves()))
					#print stri
					data[0]['noun'] = (stri)
				if temp[i].label() in adjective:
					stri = str(" ".join(temp[i].leaves()))
					data[0]['adj'] = (stri)
				if temp[i].label() == "DT":
					stri = str(" ".join(temp[i].leaves()))
					data[0]['det'] = (stri)
				if temp[i].label() == "PP":
					stri = str(" ".join(temp[i].leaves()))
					data[0]['prep'] = (stri) 				
				if temp[i].label() == "NP": 
					cc_absent(temp[i])
		else:
			if temp.label() in pronoun:
				stri = str(" ".join(temp.leaves()))
				data[0]['noun'] = (stri)
			if temp.label() in proper_noun:
				stri = str(" ".join(temp.leaves()))
				#print stri
				data[0]['noun'] = (stri)
			if temp.label() in adjective:
				stri = str(" ".join(temp.leaves()))
				data[0]['adj'] = (stri)
			if temp.label() == "DT":
				stri = str(" ".join(temp.leaves()))
				data[0]['det'] = (stri)



	def cc_present(temp):
		i=0
		# print temp
		if temp.height() > 2:
			for i in range(0,len(temp)):				
				if (temp[i].label() in  pronoun):
					stri = str(" ".join(temp[i].leaves()))
					data[1]['noun'] = (stri)
				if temp[i].label() in proper_noun:
					stri = str(" ".join(temp[i].leaves()))
					#print stri
					data[1]['noun'] = (stri)
				if temp[i].label() in adjective:
					stri = str(" ".join(temp[i].leaves()))
					data[1]['adj'] = (stri)
				if temp[i].label() == "DT":
					stri = str(" ".join(temp[i].leaves()))
					data[1]['det'] = (stri)
				if temp[i].label() == "PP":
					stri = str(" ".join(temp[i].leaves()))
					data[1]['prep'] = (stri) 				
				if temp[i].label() == "NP": 
					cc_absent(temp[i])
		else:
			if temp.label() in pronoun:
				stri = str(" ".join(temp.leaves()))
				data[1]['noun'] = (stri)
			if temp.label() in proper_noun:
				stri = str(" ".join(temp.leaves()))
				#print stri
				data[1]['noun'] = (stri)
			if temp.label() in adjective:
				stri = str(" ".join(temp.leaves()))
				data[1]['adj'] = (stri)
			if temp.label() == "DT":
				stri = str(" ".join(temp.leaves()))
				data[1]['det'] = (stri)

	c_val = -1
	for i in range(0, len(var)):
			
		if var[i].label() == "CC":
			c_val = i;
			#print("c value changed $$$$$$$")				
			break;
	if c_val == -1:	
		cc_absent(var)
	else:
		cc_absent(var[c_val-1])
		cc_present(var[c_val+1])
	
			
	
	return data

			

