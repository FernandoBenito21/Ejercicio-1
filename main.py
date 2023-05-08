from ClaseEmail import *
from claseManejaE import *


if __name__ == '__main__':
    nombre = input('Ingrese su nombre:')
    id= input('Ingrese el nombre de su cuenta:')
    dom= input('Ingrese el domnio del correo:')
    tipo= input('Input ingrese el tipo de dominio:')
    contra= input('Ingrese su contraseña:')
    email= Email(id, dom, tipo, contra)
    print("Estimado",nombre,"te enviaremos tus mensajes a la direccion",email.retornaEmail())
    email.CambiarContra()
    correo="informatica.fcefn@gmail.com"
    mail=email.crearCuenta(correo)
    validos=manejaEmail()
    validos.archivero()
    dom=input('Ingresar dominio:')
    cant=validos.ComparaDom(dom)
    print("Hay",cant,"correos con ese dominio")