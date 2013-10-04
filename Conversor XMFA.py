#Programa para fragmentar un archivo XMFA en segmentos con archivos con un solo segmento

#Carga el archivo XMFA a convertir
archivo = str(input("Dime el archivo a leer: "))
f= open(archivo, "r")
#Variable que indica si se debe o no guardar la linea leida
guardar= False
#Contador de los segmentos
cont = 0
#Bucle que lee linea a linea el archivo
 
for line in f:
#Si encuentra un comienzo de genoma y no esta activado el "guardar"
#Activa el "guardar" ya abre un nuevo archivo
    if ">" in line and not guardar:
        chunk = "L-" + str(cont)
        guardar = True
        w = open(chunk, "w")
        w.write("#" + chunk + "\n")
        cont += 1
#Si encuentra el "=", desactiva el "guardar" y cierra archivo.
    if "=" in line:
        guardar = False
        w.close()
#Si "guardar" esta activado, almacena la linea leida en el archivo
    if guardar:
        w.write(line)

f.close()
