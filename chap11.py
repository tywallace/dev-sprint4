#ch. 11
#Tyler Wallace

#11.9

def has_duplicates(l):
	d = dict()
	test = False
	for x in l:
		if x not in d:
			d[x] = 1
		else:
			test = True
	return test

fin = open('words.txt')

word_dict = dict()
for line in fin:
		word = line.strip().lower()
		word_dict[word] = word

def rotate_word(word):
	new_word = ""
	for x in word:
		if ord(x) < 91 and ord(x) > 64:
			y = chr(((ord(x)-65 + 1) % 26) + 65)
		elif ord(x) < 123 and ord(x) > 96:
			y = chr(((ord(x)-97 + 1) % 26) + 97)
		else:
			y = x
		new_word = new_word + y
	return new_word

def rotate_pair(word):
	if word in word_dict:
		if rotate_word(word) in word_dict:
			return word, new_word

for line in fin:
	word = line.strip().lower()
	print rotate_pair(word)


