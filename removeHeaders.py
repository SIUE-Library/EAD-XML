'''
Takes a txt file output from 
for file in <source>/*.tsv; do \cp -rf $file html.tsv; python getFirstWord.py; done
and edits it so it does not have any of the headers/footers:it will just have row after
row of box/folder:description data with the occasional header.  Juicy and tender.
'''

import re
def removeFooters(text):
	findURL = re.compile(r'.*[A-Z]:\\.*\n') #returns  and line that has a file location

	text = (re.sub(findURL, '', text))

	return text #no, YOU deal with this



def removeHeaders(text):
	findBlockA = re.compile('(SIUE ARCHIVES)(\n|.){1,750}([A-Z][0-9]{0,2}:( )?[0-9]{0,2})', re.I)
	print("first compiled")
	findBlockB = re.compile('(SIUE ARCHIVES)(\n|.){1,750}(Box\/Folder (Description|m?))', re.I) #returns any block going from SIUE ARCHIVES to B/F D
	print("last compiled")
	#I used 2 blocks to ensure BOTH cases get got, because there is SIGNIFICANT overlap and I don't trust python's regex engine

	text = (re.sub(findBlockB, '', text))
	print("first subbed")
	text = (re.sub(findBlockA, '', text))
	print("last subbed")
	text = re.sub("\n\n \n\n","\n",text)
	return text #no, YOU deal with this

#MAIN
out = (removeHeaders(removeFooters(open("out.txt","r").read())))
open("out.txt","w").write(out)
if "\n\n \n" in out:
	print("out")

