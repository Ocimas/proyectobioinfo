##Programa que lee un archivo backbone generado por Mauve. Devuelve 2 archivos.
#El backbone contiene los fragmentos presentes en todas cepas
#El islas devuelve si un fragmento esta presente "1" o ausente "0" en una una secuencia (solo en fragmentos no backbone)

#Lee el archivo backbone de Mauve
archivo = str(input("Dime el archivo a leer: "))
f= open(archivo, "r")

#Genera la cabecera para el backbone
cabecera = f.readline()
#Genera la cabecera para el islas
cabeceraisl = []
rango = int(len(cabecera.split())/2)
for i in range(rango):
    cabeceraisl.append(str(i))

#Guarda los backbones encontrados
resultado = []
#Guarda las filas donde hay backbones
fila = []
#Contador de filas (comienza en 1 para que coincida con excel) y para saltar la cabecera.
l= 1
#Guarda la secuencia de presencia/ausencia para las islas
islas=[]
#Guarda las filas donde hay islas
fislas=[]
#Recorre el archivo lnea a linea
for line in f:
    l += 1
    # Marcador de prsencia/ausencia de backbone
    medula = True
    #Contador de la columna
    c = 0
    linea = line.split()
    #Creamos una lista con la informacion presencia/ausencia de la linea en una secuencia
    isla = []
    #Repetimos hasta que la fila llegue a la antepenultima posición
    while c <= (len(linea)-2):
        #Comparamos las 2 columnas que tiene cada secuencia, si ambas son 0, sera isla.
        if linea[c] == "0" and linea[c+1] == "0":
            medula= False
            # No esta el fragmento en la secuencia
            isla.append("0")
        else:
            # Esta el fragmento en la secuencia
            isla.append("1")
        #Seguimos buscando hasta concluir la linea.
        c+= 2
    if medula:
        resultado.append(linea)
        fila.append(l)
    else:
        islas.append(isla)
        fislas.append(l)

f.close()

archivosal= str(input("Dime el archivo del backbone a escribir: "))
w= open(archivosal, "w")
w.write("L:\t"+cabecera)
for i in range(len(resultado)):
    w.write("L"+ str(fila[i]) + "\t" + "\t".join(resultado[i]) + "\n")
w.close()

archivosal2= str(input("Dime el archivo de islas a escribir: "))
w= open(archivosal2, "w")
w.write("L:\tseq"+"\tseq".join(cabeceraisl)+"\n")
for i in range(len(islas)):
    w.write("L"+ str(fislas[i]) + "\t" + "\t".join(islas[i]) + "\n")
w.close()
    
