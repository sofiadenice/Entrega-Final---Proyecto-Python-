from prettytable import PrettyTable
from colores import Colores
from dxLogic import Logic


class EjercicioLogic(Logic):
    def __init__(self):
        super().__init__()

    def agregarCardio(self, idUser, idEjercicio, tiempo):

        self.database.executeNonQueryBool(
            "INSERT INTO `myfitapp`.`registrousuarioejerciciocardio`(`id_registroUsuarioCardio`,`id_usuario`,`id_ejercicio`,`tiempoTotalEmpleado`,`fecha`) "
            + f"VALUES(0,{idUser},{idEjercicio}, {tiempo}, CURDATE());"
        )

    def buscardos(self, idUser, idEjercicio):

        sqlCount = f"SELECT COUNT(*) FROM myfitapp.cardiovascular WHERE id_ejercicio = '{idEjercicio}' and (id_usuario = 0 or id_usuario = '{idUser}')"

        rowsNumDic = self.database.executeQueryOneRow(sqlCount)

        rowsNum = rowsNumDic.get("COUNT(*)")
        return rowsNum

    def buscarCardio(self, EjercicioCardio, idUser):
        print("")

        busqueda = self.database.executeQueryRows(
            f"SELECT * FROM myfitapp.cardiovascular where nombreEjercicio like '%{EjercicioCardio}%'and id_usuario = 0 or id_usuario = {idUser};"
        )
        return busqueda

    def crearCardio(self, nombre, caloriasQuemadas, idUser):
        print("")

        self.database.executeNonQueryBool(
            f"INSERT INTO `myfitapp`.`cardiovascular`(`id_ejercicio`,`nombreEjercicio`,`caloriasQuemadas`,`id_usuario`) VALUES(0,'{nombre}', {caloriasQuemadas}, {idUser});"
        )

    def getFuerza(self, idUser, idEjercicio, repeticiones, series, peso):
        self.database.executeNonQueryBool(
            "INSERT INTO `myfitapp`.`registrousuarioejerciciofuerza`(`id_registroUsuarioFuerza`,`id_usuario`,`id_ejercicio`,`repeticiones`, series, pesoAplicado, `fecha`) "
            + f"VALUES(0,{idUser},{idEjercicio}, {repeticiones}, {series}, {peso}, CURDATE());"
        )

    def getBuscarFuerza(self, idUser, EjercicioPeso):
        ejercicio1 = self.database.executeQueryRows(
            f"SELECT * FROM myfitapp.fuerza where nombreEjercicio like '%{EjercicioPeso}%'and id_usuario = 0 or id_usuario = {idUser};"
        )

        return ejercicio1

    def getBuscarFuerzaDos(self, idEjercicio, idUser):
        sqlCount = f"SELECT COUNT(*) FROM myfitapp.fuerza WHERE id_ejercicio = {idEjercicio} and (id_usuario = 0 or id_usuario = {idUser});"

        rowsNumDic = self.database.executeQueryOneRow(sqlCount)

        rowsNum = rowsNumDic.get("COUNT(*)")

        return rowsNum

    def getCrearFuerza(self, nombre, parteDelCuerpo, idUser):
        self.database.executeNonQueryBool(
            f"INSERT INTO `myfitapp`.`fuerza`(`id_ejercicio`,`nombreEjercicio`,`parteDelCuerpo`,`id_usuario`) VALUES(0,'{nombre}', '{parteDelCuerpo}', {idUser});"
        )
