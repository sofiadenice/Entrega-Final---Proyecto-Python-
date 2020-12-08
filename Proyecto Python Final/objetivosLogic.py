from dxLogic import Logic


class ObjetivosLogic(Logic):
    def __init__(self):
        super().__init__()

    def getPeso(self, idUsuario):
        sqlSelect = f"SELECT * FROM myfitapp.usuario WHERE id_usuario = '{idUsuario:}'"

        selectUserDic = self.database.executeQueryOneRow(sqlSelect)

        pesoActual = selectUserDic.get("pesoActual")

        return pesoActual

    def getPesoDeseado(self, idUsuario):
        sqlSelect = f"SELECT * FROM myfitapp.usuario WHERE id_usuario = '{idUsuario:}'"

        selectUserDic = self.database.executeQueryOneRow(sqlSelect)

        pesoDeseado = selectUserDic.get("pesoDeseado")

        return pesoDeseado

    def getAltura(self, idUsuario):
        sqlSelect = f"SELECT * FROM myfitapp.usuario WHERE id_usuario = '{idUsuario:}'"

        selectUserDic = self.database.executeQueryOneRow(sqlSelect)

        altura = selectUserDic.get("altura")

        return altura

    def cambiarIntensidad(self, intensidad, idUsuario):

        sqlUpdate = f"UPDATE myfitapp.usuario SET intensidad = {intensidad} WHERE id_usuario = {idUsuario:}"

        result = self.database.executeNonQueryBool(sqlUpdate)

        return result

    def cambiarPesoDeseado(self, pesoDeseado, idUsuario):

        sqlUpdate = f"UPDATE myfitapp.usuario SET pesoDeseado = {pesoDeseado} WHERE id_usuario = {idUsuario:}"

        result = self.database.executeNonQueryBool(sqlUpdate)

        return result

    def getIntensidad(self, idUsuario):

        sqlSelect = f"SELECT * FROM myfitapp.usuario WHERE id_usuario = '{idUsuario:}'"

        selectUserDic = self.database.executeQueryOneRow(sqlSelect)

        intensidad = selectUserDic.get("intensidad")

        return intensidad

    def selectEjercicios(self, intensidad):

        sqlSelect = f"SELECT * FROM myfitapp.objetivos WHERE intensidad = {intensidad:}"

        selectUserDic = self.database.executeQueryRows(sqlSelect)

        return selectUserDic
