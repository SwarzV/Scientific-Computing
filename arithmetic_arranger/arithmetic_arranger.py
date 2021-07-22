
def arithmetic_arranger(a, soluciones=False):

	if len(a) > 5:
		return("Error: Too many problems.")
	else:
		primera = []
		operador = []
		segunda = []
		igual = "-"
		resultado = []
		num = 0

		for h in a:
			x = a[num].split()
			primera.append(x[0])
			operador.append(x[1])
			segunda.append(x[2])
			try:
				int(primera[num])
			except ValueError:
				print(primera[num])
				return "Error: Numbers must only contain digits."
			try:
				int(segunda[num])
			except ValueError:
				return "Error: Numbers must only contain digits."
			if operador[num] == "+":
				resultado.append((int(primera[num]) + int(segunda[num])))
			elif operador[num] == "-":
				resultado.append((int(primera[num]) - int(segunda[num])))
			else:
				return("Error: Operator must be '+' or '-'.")

			if int(primera[num]) > 9999 or int(segunda[num]) > 9999:
				return("Error: Numbers cannot be more than four digits.")
			num += 1
		num = 0

		for h in a:
			print(primera[num].rjust(6), end="    ")
			num += 1
		num = 0
		print ("")
		for h in a:
			print(operador[num], segunda[num].rjust(4), end="    ")
			num += 1
		print("")
		num = 0
		for h in a:
			if len(str(primera[num])) > len(str(segunda[num])):
				print(igual.rjust(6,"-"), end="    ")
			else:
				print(igual.rjust(6,"-"), end="    ")
			num += 1
		num = 0
		print("")
		if soluciones:	
			for h in a:
				print(str(resultado[num]).rjust(6), end="    ")
				num += 1 

arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True)