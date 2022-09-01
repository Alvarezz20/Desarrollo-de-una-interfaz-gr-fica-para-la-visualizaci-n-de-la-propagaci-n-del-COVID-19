	import time
	import pandas as pandas_d
	from influxdb import InfluxDBClient
	
	client = InfluxDBClient(host="localhost",port=8086)
	client.switch_database("Ejemplo")
	
	file = pandas_d.read_csv("EV_001.csv")
	file.dropna(inplace=True)
	print(file.shape)
	
	
	for row_ind, row in file.iloc[1:].iterrows():
	json_body=[{
		"measurement":"EV_01",
		"tags":{"ID_Individuo":row[0]},
		"fields":{
			"Nombre":row[0],
			"Latitude":row[2],
			"Longitude":row[3],
			"Metrica":row[4]
		},
		"Tiempo": row[6]
	}]
	
	
	client.write_points(json_body)
	print("Subida realizada con exito")
	end = time.time()
	print("Tiempo de ejecucion:")
	print(end - start)
	print("segundos")
