#Programa para sacar el encabezado de los fragmentos de XFMA

#Numero de fragmentos creados, se supone que el primer fragmento es el 0
Ninput = input("Dime el numero del ultimo fragmento: ")
Nfrag = range(int(Ninput)+1)
#Secuencia a tomar como referencia para el ordenamiento
sec= input("Dime el numero de la secuencia a tomar como referencia: ")
#Variable con el nombre del fichero a ser leido
fich = ""
#Almacen de fragmento
frag= ""
#Lista para almacenar las listas de todos los fragmentos
#Una lista para cada fragmento
fraglist = []
#Lista para almacenar temporalmente las lineas de un fragmento
temp = []
#Recorro todos los archivos nombrados
for i in Nfrag:
    #Abro los ficheros con el nombre correspondiente
    frag = "L-" + str(i)
    fich = frag
    f = open(fich,"r")
    #Recorro las lineas del fichero
    for line in f:
        #Si es el encabezado, lo leo y añado a la lista temporal
        if ">" in line:
            temp.append(line)
    #Añado la lista temporal a la lista de listas de fragmentos
    fraglist.append(temp)
    #Reinicio la lista temporal
    temp = []
    f.close()

#Creo el fichero de salida
sal = open("Salida", "w")
ordenfrag = []
listapos = []
#Recorro la lista de listas de fragmentos
for i in range(len(fraglist)):
    #Escribo el fragmento que es
    sal.write("L:" + str(i) + "\n")
    #Recorro cada lista
    for j in fraglist[i]:
        #Separo y escribo las lineas añadidas
        linea = j.split()
        sal.write(str(linea) + "\n")
        if (sec + ":") in linea[1]:
            pos = linea[1].split(:)
            pos = pos[1].split(-)
            ordenfrag.append(j)
            listapos.append(pos)
        
sal.close()

##### FALTA ORDENAR
        
