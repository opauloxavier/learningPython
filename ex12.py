numero = raw_input("Informe quantos metros deseja converter: ")

if numero is None:
	print "E necessario digitar o numero de metros"

print "Diga a unidade de saida desejada: J- jardas F- pes"
saida = raw_input(" > ")

def converte(saida,numero):
	if saida.lower() == "j":
		print "%d metros equithvalem a %r jardas" %(int(numero),float(numero)*0.9144)

	elif saida.lower() == "f" :
		print "%d metros equivalem a %r pes" %(int(numero),float(numero)*0.3048)


converte(saida,numero)