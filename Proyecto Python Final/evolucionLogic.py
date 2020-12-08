from dxLogic import Logic


class EvolucionLogic(Logic):
    def __init__(self):
        super().__init__()

    def evoPeso(self, idUsuario):
        sql = f"select * from registrodiario where id_usuario = {idUsuario} order by fecha asc;"
        datos = self.database.executeQueryRows(sql)
        return datos

    def evoCintura(self, idUsuario):
        sql = f"select * from registrodiario where id_usuario = {idUsuario} order by fecha asc;"
        datos = self.database.executeQueryRows(sql)
        return datos

    def evoCuello(self, idUsuario):
        sql = f"select * from registrodiario where id_usuario = {idUsuario} order by fecha asc;"
        datos = self.database.executeQueryRows(sql)
        return datos

    def evoCalConsumidas(self, idUsuario):
        sql = (
            "SELECT consumoalimento.fecha,sum(consumoalimento.porcion*producto.calorias) as caloriasTotales "
            + "FROM consumoalimento inner join producto on consumoalimento.id_producto = producto.id_producto "
            + f"where consumoalimento.id_usuario = {idUsuario} group by consumoalimento.fecha order by fecha asc;"
        )
        datos = self.database.executeQueryRows(sql)
        return datos

    def evoCalQuemadas(self, idUsuario):
        sql = (
            "SELECT registrousuarioejerciciocardio.fecha, sum(cardiovascular.caloriasQuemadas*registrousuarioejerciciocardio.tiempoTotalEmpleado) as quemadasTotales "
            + "FROM registrousuarioejerciciocardio inner join cardiovascular on registrousuarioejerciciocardio.id_ejercicio = cardiovascular.id_ejercicio "
            + f"WHERE registrousuarioejerciciocardio.id_usuario = {idUsuario} GROUP BY registrousuarioejerciciocardio.fecha order by fecha asc;"
        )
        datos = self.database.executeQueryRows(sql)
        return datos

    def evoEjPeso(self, idUsuario):
        sql = (
            "SELECT * "
            + "FROM registrousuarioejerciciofuerza inner join fuerza on registrousuarioejerciciofuerza.id_ejercicio = fuerza.id_ejercicio "
            + f"WHERE registrousuarioejerciciofuerza.id_usuario = {idUsuario} order by registrousuarioejerciciofuerza.fecha asc;"
        )

        datos = self.database.executeQueryRows(sql)
        return datos
