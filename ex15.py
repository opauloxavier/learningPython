from sys import argv

def print_two(*args):
	arg1,arg2=args
	print "arg1: %r, arg2: %r" % (arg1,arg2)

def print_two_again(arg1,arg2):
	print "arg1:%r, arg2:%r" % (arg1,arg2)

def print_one(arg1):
	print "arg1:%r" %arg1

def print_none():
	print "No donuts for you"

print_two("ha","he")
print_two_again("zed","ahri")
print_one("YESS")
print_none()