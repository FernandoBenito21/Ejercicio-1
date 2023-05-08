class Email:
    def __init__(self, id, dom, tipo, contra):
        self.__idCuenta=id
        self.__dominio=dom
        self.__tipoDominio=tipo
        self.__contraseña=contra

    def retornaEmail(self):
        return self.__idCuenta+"@"+self.__dominio+"."+self.__tipoDominio

    def getDominio(self):
        return self.__dominio

    def CambiarContra(self):
        contra_actual= input('Ingresar su contraseña actual:')
        if (contra_actual== self.__contraseña):
            self.__contraseña= input('Ingrese su nueva contraseña:')
            print("La contraseña se ha modificado exitosamente")
        else:
            print("La contraseña ingresada no coincide con la contraseña actual")
            return (None)

    def crearCuenta(self, email):
        id=email.split("@")[0]
        dom=email.split("@")[1].split(".")[0]
        tipo=email.split("@")[1].split(".")[1]
        contra="1234"
        self.__cuenta=Email(id,dom,tipo,contra)
        return self.__cuenta
