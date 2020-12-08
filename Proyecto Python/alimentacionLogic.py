# from databaseX import DatabaseX
from prettytable import PrettyTable
from colores import Colores
from dxLogic import Logic


class AlimentacionLogic(Logic):
    def __init__(self):
        super().__init__()

    def getAgregar(self, idAlimento, idUser, porcion):
        self.database.executeNonQueryBool(
            "INSERT INTO `myfitapp`.`consumoalimento`(`id_consumoAlimento`,`id_producto`,`id_usuario`,`porcion`,`fecha`) "
            + f"VALUES(0,{idAlimento},{idUser},{porcion}, CURDATE());"
        )

    def getBuscar(self, idUser, alimento):

        busqueda = self.database.executeQueryRows(
            f"SELECT * FROM myfitapp.producto WHERE nombre like '%{alimento}%' and id_usuario = 0 or id_usuario = {idUser};"
        )

        return busqueda

    def getBuscarDos(self, idAlimentacion, idUser):

        sqlCount = f"SELECT COUNT(*) FROM myfitapp.producto WHERE id_producto = {idAlimentacion} and (id_usuario = 0 or id_usuario = {idUser});"

        # Imprime para comprobar estructura del sqlCount
        # print(sqlCount)

        rowsNumDic = self.database.executeQueryOneRow(sqlCount)

        # Imprime el diccionario resultante de ejecutar sqlCount
        # print(rowsNumDic)

        rowsNum = rowsNumDic.get("COUNT(*)")

        # Imprime el numero de filas con ese ID de alimento
        # print(rowsNum)
        return rowsNum

    def crearReceta(
        self,
        nombre,
        porciones,
        calorias,
        grasaTotales,
        colesterol,
        sodio,
        azucares,
        idUser,
    ):

        self.database.executeNonQueryBool(
            "INSERT INTO `myfitapp`.`producto`(`id_producto`,`nombre`,`porcion`,`calorias`,`grasasTotales`,`colesterol`,`sodio`,`azucares`,`id_usuario`) "
            + f"VALUES(0,'{nombre}', {porciones}, {calorias}, {grasaTotales}, {colesterol}, {sodio},{azucares}, {idUser});"
        )
