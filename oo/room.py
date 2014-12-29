class room(object):

	totalSalas=0

	def __init__(self,numero):
		self.numero=numero
		self.capacidade = 40
		room.totalSalas+=1

	def numeroSala(self):
		return self.numero

salaAula = room(80)
salaAula2 = room(60)
salaAula3 = room(50)
salaAula4 = room(50)

print room.totalSalas

print salaAula4.capacidade