from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copiando %s to %s" %(from_file,to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d long" %len(indata)

print "Does the output file exist? %r" %exists(to_file)

out_file = open(to_file,'w')
out_file.write(indata)

print "Feito"

out_file.close()
in_file.close()