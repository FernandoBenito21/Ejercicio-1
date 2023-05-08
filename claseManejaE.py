from ClaseEmail import *
import csv

class manejaEmail:
    def __init__(self):
        self.__listaEmail= []
    def agregarEmail(self,unEmail):
        self.__listaEmail.append(unEmail)
    def archivero(self):
        archivo= open('Correos_ej1.csv')
        lector= csv.reader(archivo,delimiter=',')
        for elemento in lector:
            id= elemento[0]
            dom= elemento[1]
            tipo= elemento[2]
            contra= elemento[3]
            unEmail= Email(id,dom,tipo,contra)
            if unEmail is not None:
                self.agregarEmail(unEmail)
            else:
                print("La direccion de correo",elemento,"no es valida")
        archivo.close()
    def ComparaDom(self,dom):
        i=0
        cant=0
        for i in range(len(self.__listaEmail)):
            if(self.__listaEmail[i].getDominio()==dom):
                cant=cant+1
        return cant