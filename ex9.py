from sys import argv

script, first, second, third = argv

total=raw_input("bet on the total:")

result= int(total) == (int(first)+int(second)+int(third))

print "The script is called:", script
print "Your sum is:", int(first)+int(second)+int(third)

print "Your bet was:", result

print "Because you're happy"