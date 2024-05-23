#Partidos_ganados = int(input("Ingrese la cantidad de partidos ganados"))
#Partidos_empatados = int(input("Ingrese la cantidad de partidos empatados"))
#a = (Partidos_ganados*3)
#print(a+Partidos_empatados)

#Var_a = int(input("Ingrese un numero entero a sumar"))
#Var_b = int(input("Ingrese un numero entero a sumar"))
#print (Var_a * Var_b)

#Total_Factura = float(input("Hola! este es un programa para calcular propina, por favor ingrese el monto de su factura $"))
#Calculo = ((Total_Factura * 20 )/100)
#print("La propina que tiene que dejar es de $",Calculo)

#lista_de_Provincias_Arg = ["Chubut","Catamarca","La Rioja","Santan Cruz","Buenos Aires","La Pampa"]
#print(lista_de_Provincias_Arg)
#print(lista_de_Provincias_Arg[3])
#print(lista_de_Provincias_Arg[2:4])
#print(type(lista_de_Provincias_Arg))
#print(lista_de_Provincias_Arg[:4])
#lista_de_Provincias_Arg.append("La Pampa")
#lista_de_Provincias_Arg.append("Misiones")
#lista_de_Provincias_Arg.insert(4,"Tucuman")
#lista2 =["Tierra del fuego","Santa Fe","Entre Rios"]
#lista_de_Provincias_Arg.extend(lista2)
#del(lista_de_Provincias_Arg[1])
#UltimaProvincia = lista_de_Provincias_Arg.pop()
#print(UltimaProvincia)


#tupla1 = (1,2,3,4,5,6)
#print(type(list(tupla1)))

#Tupla_Numeros_Enteros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
#print(Tupla_Numeros_Enteros[10:15])
#print(Tupla_Numeros_Enteros.count(1))
#print(list(Tupla_Numeros_Enteros))
#PrimerNumero = Tupla_Numeros_Enteros[0]
#SegundoNumero = Tupla_Numeros_Enteros[1]
#TercerNumero = Tupla_Numeros_Enteros[2]
#print(PrimerNumero)

#diccionarioOne = {"joaquin":42984393,"Lucas": 13571293}
#print("joaquin" in diccionarioOne)

#Diccionario_Datos = {"Nombre":"Joaquin Santana","Edad":22, "Carrera":"Tecnicatura Ciencia de datos e IA"}
#print(Diccionario_Datos)
#print(Diccionario_Datos.get("Nombre"))
#Diccionario_Datos["Edad"]= 24
#print(Diccionario_Datos)
#Diccionario_Datos["Sexo"]= "Masculino"
#print(Diccionario_Datos)
#Diccionario_Datos.pop("Edad")
#print(Diccionario_Datos)


Diccionario_Notas ={"Programacion 2": 9,"Ciencia de Datos":8,"Programacion 1": 10}
print(Diccionario_Notas)
Nuevo_diccionario = Diccionario_Notas.copy()
print(Nuevo_diccionario)
print(Nuevo_diccionario.values())
print(len(Nuevo_diccionario))

