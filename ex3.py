from datetime import datetime

my_name="Paulo"
my_age=23
my_height=181
my_weight= 30
my_eyes="Brown"
my_teeth="white"
my_hair="Brown"


def date():
	now = datetime.now()
	print "Date now: %s/%s/%s" % (now.day,now.month,now.year)
	

date()


#testando as funcoes do github