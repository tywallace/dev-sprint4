#Ch10
#Tyler Wallace

#10.7

def is_anagram(str1,str2):
	a = list(str1)
	b = list(str2)
	a.sort()
	b.sort()
	if a == b:
		return True
	else:
		return False

fin = open('words.txt')
line = fin.readline()

word_list = []
for line in fin:
		word = line.strip()
		word_list.append(word)

inter_list = []

def is_interlock(str):
	a = list(str)
	even, odd = a[::2],a[1::2]
	even = ''.join(even)
	odd = ''.join(odd)
	if even in word_list and odd in word_list:
		print str
		inter_list.append(str)


for word in word_list:
	is_interlock(word)

print inter_list




