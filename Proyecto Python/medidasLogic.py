from dxLogic import Logic


class MedidasLogic(Logic):
    def __init__(self):
        super().__init__()

    def ingresarPrimerPeso(self, peso, idUsuario):
        cintura = 0.00
        cuello = 0.00
        sql = (
            "INSERT INTO `myfitapp`.`registrodiario`(`id_registro`,`id_usuario`,`cintura`,`cuello`,`pesoActual`,`fecha`) "
            + f"VALUES(0,{idUsuario},{cintura},{cuello},{peso},curdate());"
        )
        self.database.executeNonQueryBool(sql)

    def existenciaRegistro(self, idUsuario):
        sqlCount = f"SELECT COUNT(id_registro) from registrodiario where fecha = curdate() and id_usuario = {idUsuario};"
        datos = self.database.executeQueryOneRow(sqlCount)
        count = datos.get("COUNT(id_registro)")
        return count

    def ingresarPeso(self, peso, idUsuario):
        cintura = 0.00
        cuello = 0.00

        count = self.existenciaRegistro(idUsuario)

        if count == 0:
            sql = (
                "INSERT INTO `myfitapp`.`registrodiario`(`id_registro`,`id_usuario`,`cintura`,`cuello`,`pesoActual`,`fecha`) "
                + f"VALUES(0,{idUsuario},{cintura},{cuello},{peso},curdate());"
            )
            self.database.executeNonQueryBool(sql)
        else:
            sql = (
                "UPDATE `myfitapp`.`registrodiario` "
                + f"SET `pesoActual` = {peso} where `fecha` = curDate() AND `id_usuario` = {idUsuario};"
            )
            self.database.executeNonQueryBool(sql)

        # Actualización del campo Peso Actual en la tabla Usuario

        sql1 = (
            "UPDATE `myfitapp`.`usuario` "
            + f"SET `pesoActual` = {peso} where `id_usuario` = {idUsuario};"
        )
        self.database.executeNonQueryBool(sql1)

    def ingresarCintura(self, cintura, idUsuario):
        peso = 0.00
        cuello = 0.00

        count = self.existenciaRegistro(idUsuario)

        if count == 0:
            sql = (
                "INSERT INTO `myfitapp`.`registrodiario`(`id_registro`,`id_usuario`,`cintura`,`cuello`,`pesoActual`,`fecha`) "
                + f"VALUES(0,{idUsuario},{cintura},{cuello},{peso},curdate());"
            )
            self.database.executeNonQueryBool(sql)
        else:
            sql = (
                "UPDATE `myfitapp`.`registrodiario` "
                + f"SET `cintura` = {cintura} where `fecha` = curDate() AND `id_usuario` = {idUsuario};"
            )
            self.database.executeNonQueryBool(sql)

    def ingresarCuello(self, cuello, idUsuario):
        peso = 0.00
        cintura = 0.00

        count = self.existenciaRegistro(idUsuario)

        if count == 0:
            sql = (
                "INSERT INTO `myfitapp`.`registrodiario`(`id_registro`,`id_usuario`,`cintura`,`cuello`,`pesoActual`,`fecha`) "
                + f"VALUES(0,{idUsuario},{cintura},{cuello},{peso},curdate());"
            )
            self.database.executeNonQueryBool(sql)
        else:
            sql = (
                "UPDATE `myfitapp`.`registrodiario` "
                + f"SET `cuello` = {cuello} where `fecha` = curDate() AND `id_usuario` = {idUsuario};"
            )
            self.database.executeNonQueryBool(sql)
