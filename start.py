import os
import spn_knowledgeBase as spn

os.system('cls' if os.name == 'nt' else 'clear')
print "\n\n"
print "talkie 1.0"
print "-----------------------------------------------------------------------------------------------------\n"
print '''hi there !
	takie is your personal assistant that can remember evrything that is told to it and can help 
	you out whenever you need any help regarding the things you told to it remember.. Just a few
	instructions that will help you out 

	Commands : 
	:R   ->  Change to the record mode
	:Q   ->  Change to question/answer mode
	
	Once in the record mode, [ :) ] appears which indicates that the system is read to take questions.
	While [ // ] appears in the question/answer mode
	
	:D   ->  Delete the existing information told to `talkie`
	:A   ->  See all the information currently with `talkie`
	:X   ->  Exit

	'''

# 1 - record mode, 0 - qa mode
mode = 1

spn.knowledgeBase = []

# :d
def emptyKnowledgeBase() :
	spn.knowledgeBase = []
	print "knowledge base emptied."

# :a
def printKnowledgeBase() :
	spn.prnt()

# :q
def queryKnowledgeBase(sentence) :
	tokens = sentence.split(' ')
	spn.query(tokens)


while True :

	# set the current mode !
	if mode is 1 :
		print '\n[ :) ]',
	else :
		print '\n[ // ]',

	# take the input from the user 
	inp = raw_input()

	if inp[0] is ':' :
		if len(inp) is 2 :
			if inp[1] is 'R' or inp[1] is 'r':
				mode = 1
				continue
			elif inp[1] is 'Q' or inp[1] is 'q':
				mode = 0
				continue
			elif inp[1] is 'D' or inp[1] is 'd':
				print "deleting the complete knowledge base ..."
				emptyKnowledgeBase()
			elif inp[1] is 'A' or inp[1] is 'a':
				 printKnowledgeBase()
			elif inp[1] is 'X' or inp[1] is 'x':
				print "exiting ..."
				break
			else :
				print "invalid command !.. please try again."
				continue

		else :
			print "invalid command !.. please try again."
			continue

	else :
		if mode is 1 :
			try :
				spn.addToKB(inp)
				print "added. :)"
			except Exception, e :
				print "Cannot parse this. please try some other sentence :("
		else :
			queryKnowledgeBase(inp)

