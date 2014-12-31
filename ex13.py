from sys import argv

script,filename = argv

print "Deletando %r",filename

print "Cancele com ctrl-c"
print "Se desejar continuar, aperte enter"

raw_input("?")

print "Opening the file.."
target = open(filename,'w')

print "Trucanting the file. "
target.truncate()

print "Give me three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "lets go lets go"

target.write(line1+"\n")
target.write(line2+"\n")
target.write(line3+"\n")