from dxLogic import Logic


class SignUpLogic(Logic):
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

    def insertUser(
        self,
        nombre,
        apellido,
        correo,
        user,
        contra,
        genero,
        altura,
        peso,
        pesoDeseado,
        anno,
        mes,
        dia,
    ):

        sql2 = (
            "INSERT INTO myfitapp.usuario (id_usuario, nombre, apellido, correo, user, contra, id_genero, altura, pesoActual, pesoDeseado, nacimiento, premium)"
            + f"VALUES (0, '{nombre}', '{apellido}', '{correo}', '{user}', '{contra}', {genero}, {altura}, {peso}, {pesoDeseado}, '{anno}-{mes}-{dia}', curdate());"
        )

        insert = self.database.executeNonQueryBool(sql2)

        return insert

    def getID(self, user):
        sqlId = f"SELECT id_usuario from myfitapp.usuario where user = '{user}';"

        IdUsuarioDic = self.database.executeQueryOneRow(sqlId)
        idUser = IdUsuarioDic.get("id_usuario")

        return idUser
