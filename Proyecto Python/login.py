from loginLogic import LoginLogic


class Login:
    def __init__(self):
        self.idUser = 0
        self.logic = LoginLogic()
        pass

    def comprobacion(self, usuario, contra):

        rowsNum = self.logic.sqlCount("user", usuario)

        if rowsNum == 1:

            contraBD = self.logic.getContra(usuario)

            if contraBD == contra:

                idBD = self.logic.getUserID(usuario)
                self.idUser = idBD
                return True

            else:
                print("Contraseña incorrecta")
                return False

        else:
            print("El usuario que ha ingresado no existe")

    def idUsuario(self):
        return self.idUser
