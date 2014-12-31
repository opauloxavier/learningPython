poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print 10*"-"


five = 10-2+3-6
print five

def secret_formula(started):
	x = started*500
	jars = x/1000
	crates = jars/100
	return x,jars,crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print beans,jars,crates

beans, jars, crates = secret_formula(start_point/10)

print beans,jars,crates