states = {
	'Rio de Janeiro': 'RJ',
	'Florida': 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
	'RJ': 'Nova Iguacu'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-'*10
print 'NY state has: ', cities['NY']
print 'OR state has: ', cities['OR']

print'-'*10
print "Michingan has: ",cities[states['Michigan']]
print "Florida has: ",cities[states['Florida']]

print '-'*10
for state, abbrev in states.items():
	print "%s is %s" %(state,abbrev)

print '-'*10
for abbrev,city in cities.items():
	print "%s has the city %s" %(abbrev,city)

print '-'*10
for state,abbrev in states.items():
	print "%s state is %s and has %s" %(state,abbrev,cities[abbrev])

state = states.get('Texas')

if not state:
	print "No donuts for you"

city = cities.get('TX','NOPE')
print "The city for 'TX' is: %s" %city