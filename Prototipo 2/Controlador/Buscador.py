from arxiv import *
import urllib
texto= raw_input("Ingrese texto de busqueda: ")
maximo=int (raw_input("Ingrese maximo de resultados: "))
a= arxiv.query( texto, prune=True, start=0, max_results= maximo)
print a
for i in range(0, maximo):
	print "---- Resultado %d----" % (i) 
	b= a[i]
	print b['title']
	print b['pdf_url']
	print "---------------------"
