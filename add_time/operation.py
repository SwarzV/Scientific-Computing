tiempo = 10
añadir = 30

horas = tiempo + añadir

hora = horas % 24
 
print(hora)

if hora > 12:
	hora -= 12
	print("tarde", hora)
elif hora < 12:
	print("mañana")
