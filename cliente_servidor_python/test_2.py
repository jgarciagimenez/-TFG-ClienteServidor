def solicitarFirewall():

	print (nivelActual[6])

	if nivelActual[6] == '1' or nivelActual[6] == '2' or nivelActual[6] == '4':
		return """Cortafuegos sensados"""
	elif nivelActual[6] == '3':
		return """Cortafuegos me"""
	elif nivelActual[6] == '5 ' or nivelActual[6] == ' 6':
		return """Cortafuegos """
	else:
		return "asdf"


nivelActual = 'defcon3'
asdf = solicitarFirewall()
print (asdf)


