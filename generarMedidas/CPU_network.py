import psutil 

outfile_CPU = open ('CPU.txt','w')
outfile_sent = open ('sent_bytes.txt','w')
outfile_received = open ('received_bytes.txt','w')



try: 
	aux1 = psutil.net_io_counters(pernic=True)['enp0s3'][0]
	aux2 = psutil.net_io_counters(pernic=True)['enp0s3'][1]

	while True:

		# outfile_CPU.write(str(psutil.cpu_percent(interval=1))+'\n')
		
		valor1 = psutil.net_io_counters(pernic=True)['enp0s3'][0] - aux1 
		aux1 = psutil.net_io_counters(pernic=True)['enp0s3'][0]
		
		valor2 = psutil.net_io_counters(pernic=True)['enp0s3'][1] - aux2 
		aux2 = psutil.net_io_counters(pernic=True)['enp0s3'][1]

		print ('CPU: '+ str(psutil.cpu_percent(interval=1)))	
		print ('Sent bytes: ' + str(valor1))
		print ('Received bytes: ' + str(valor2) + '\n')

		outfile_CPU.write(str(psutil.cpu_percent(interval=1)) + '\n')
		outfile_sent.write(str(valor1) + '\n')
		outfile_received.write(str(valor2) + '\n')

except:

	print ('Programa interrumpido, creando fichero')
	outfile_CPU.close
	outfile_sent.close
	outfile_received.close