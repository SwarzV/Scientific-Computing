def add_time(a, b, c = 1):
	part = a.partition(" ")
	part2 = part[0].partition(":")
	horas_part = part2[0].partition(":")
	minutos_part = part2[2].partition(":")
	momento = part[2]
	horas = int((horas_part[0]))
	minutos = int((minutos_part[0]))
	add_part = b.partition(":")
	add_horas = int(add_part[0])
	add_minutes = int(add_part[2])
	dias_semana = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
	dias_extra = 0
	if momento == "PM":
		horas += 12
	minutos = (minutos + add_minutes)
	horas = (horas + add_horas)
	if minutos >= 60:
		horas_extra = (minutos // 60)
		minutos = (minutos % 60)
		horas = (horas + horas_extra)
	if horas > 24:
		dias_extra = (horas // 24)
		res_horas = (horas % 24)
	elif horas <= 24:
		res_horas = horas
	if res_horas < 12:
		momento = "AM"
	if res_horas > 12:
		momento = "PM"
		res_horas -= 12
	if (horas // 12) == 1:
		momento = "PM"
	elif (horas // 12) == 2:
		momento = "AM"
	if res_horas == 0:
		res_horas = 12
	if dias_extra > 0 and c != 1:
		indice_dia = (dias_semana.index(c.lower()) + dias_extra)
		dia_def = (indice_dia % 7)
		dia = dias_semana[dia_def]
	elif dias_extra == 0 and c != 1:
		dia_def = dias_semana.index(c.lower())
		dia = dias_semana[dia_def]
	if c == 1:
		if dias_extra == 0:
			z = str(res_horas) +":" + str(minutos).zfill(2) + " " + str(momento)
		elif dias_extra == 1:
			z = str(res_horas) +":" + str(minutos).zfill(2) + " " + str(momento) + " " + "(next day)"
		elif dias_extra > 1:	
			z = str(res_horas) +":" + str(minutos).zfill(2) + " " + str(momento) + " " + "(" + str(dias_extra) + " days later)"
	if c != 1:
		if dias_extra == 0:
			indice_dia = dias_semana.index(c.lower())
			z = str(res_horas) +":" + str(minutos).zfill(2) + " " + str(momento) + ", " + str(dia.capitalize())
		elif dias_extra == 1:
			z = str(res_horas) +":" + str(minutos).zfill(2) + " " + str(momento) + ", " + str(dia.capitalize()) + " " + "(next day)"
		elif dias_extra > 1:
			z = str(res_horas) +":" + str(minutos).zfill(2) + " " + str(momento) + ", " + str(dia.capitalize()) + " " + "(" + str(dias_extra) + " days later)"
	return z