defcon = "CONTROL asgf"


if defcon.startswith("CONTROL") and defcon.split(' ', 1)[1].isdigit() and int(defcon.split(' ', 1)[1]) > 0 and int(defcon.split(' ', 1)[1]) <4 : 
	print (defcon.split(' ',1)[1])

else : 
	print (" comando incorrecto")

