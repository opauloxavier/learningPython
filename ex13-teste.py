from os.path import exists

def copiaTxt(from_file,to_file):
	if exists(from_file):
		copiedFile=open(from_file)
		copiedData=copiedFile.read()

		to_file=open(to_file,'w')
		to_file.write(copiedData)


copiaTxt("teste.txt","arquivo_copiado.txt")