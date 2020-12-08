from dxLogic import Logic


class LoginLogic(Logic):
    def __init__(self):
        super().__init__()

    def sqlCount(self, campo, registro):

        sqlCount = (
            f"SELECT COUNT(*) FROM myfitapp.usuario WHERE {campo:} = '{registro:}'"
        )

        # Imprime para comprobar estructura del sqlCount
        # print(sqlCount)

        rowsNumDic = self.database.executeQueryOneRow(sqlCount)

        # Imprime el diccionario resultante de ejecutar sqlCount
        # print(rowsNumDic)

        rowsNum = rowsNumDic.get("COUNT(*)")

        # Imprime el numero de filas con ese nombre de usuario
        # print(rowsNum)

        return rowsNum

    def getContra(self, usuario):

        sqlSelect = f"SELECT * FROM myfitapp.usuario WHERE user = '{usuario:}'"

        selectUserDic = self.database.executeQueryOneRow(sqlSelect)

        # Imprime el diccionario que resulta de ejecutar sqlSelect
        # print(selectUserDic)

        contraBD = selectUserDic.get("contra")

        # Imprime la contraseña de la BD
        # print(contraBD)

        return contraBD

    def getUserID(self, usuario):
        sqlSelect = f"SELECT * FROM myfitapp.usuario WHERE user = '{usuario:}'"

        selectUserDic = self.database.executeQueryOneRow(sqlSelect)

        # Imprime el diccionario que resulta de ejecutar sqlSelect
        # print(selectUserDic)

        idUser = selectUserDic.get("id_usuario")

        # Imprime la contraseña de la BD
        # print(contraBD)

        return idUser