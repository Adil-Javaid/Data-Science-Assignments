# 30-9-2023
# CSC461 – Assignment2 – Regular Expressions
# H. M. Adil Javaid
# FA21-BSE-006
# Extarct, remove, and replace different words in file through regular expression

import re

file = open("C:/Users/Adil/Desktop/FA21-BSE-006/5th Semester/Data Science/Assignment/example-text.txt","r").read()

# 1) Extract list of all words.
all_Words = re.findall(r"\w+",file)
print("1) List of all words:\n",all_Words)

# 2) Extract list of all words starting with the capital letter
capitalletters = re.findall(r"[A-Z]\w+",file)
print("\n2) Start with capital letters:\n",capitalletters)

# 3) Extract list of all words of length 5
length = re.findall(r"\b\w{5}\b",file)
print("\n3) List of all words with length 5:\n",length)


# 4) Extract list of all words inside double qoutes
doubeQuotes = re.findall(r'"([^"]+)"',file)
print("\n4) List of all words in double quotes:\n",doubeQuotes)

# 5) List of all vowels
vowels = re.findall(r"\b[a,e,i,o,u,A,E,I,O,U]\w+\b",file)
print("\n5) List of all vowels:\n",vowels)

# 6) Extract list of 3 letter words ending with letter ‘e’
endOfe = re.findall(r'\b\w\we\b',file)
print("\n6) list of 3 letter words ending with letter 'e':\n",endOfe)

# 7) Extract list of all words starting and ending with letter ‘b’
startEndb = re.findall(r"\b[b]\w+[b]\b",file)
print("\n7) list of all words starting and ending with letter 'b':\n",startEndb)
#Also
startb = re.findall(r"\b[b]\w+\b",file)
print("\n7) list of all words starting with letter 'b':\n",startb)
endb = re.findall(r"\b\w+[b]\b",file)
print("\n7) list of all words ending with letter 'b':\n",endb)


# 8) Remove all the punctuation marks from the text
punctuation = re.sub(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/\|~-]','',file)
print("\n8) Remove all the punctuation marks from the text:\n",punctuation)

# 9) Replace all words ending ‘n't’ to their full form ‘not’
replace = re.sub(r"n't"," not",file)
print("\n9) Replace all words ending 'n't' to their full form 'not':\n",replace)

# 10) Replace all the new lines with a single space
replace = re.sub(r"\n","",file)
print("\n10) Replace all the new lines with a single space:\n",replace)
