from sys import argv

script,filename=argv

file = open(filename)
file_read = file.read()

def break_words(a):
	a = a.split(' ')
	return a

def sort_words(a):
	return sorted(a)

def print_word(a):
	print a.pop(0)

def print_last(a):
	print a.pop(-1)

def sort_sentence(a):
	x=break_words(a)
	print sort_words(x)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_word(sentence)
	print_last(sentence)

b=break_words(file_read)

b[2] = "INTRUSO"

print b
##print sort_words(b)

#print sort_words("testing some fucking text")