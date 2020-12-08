from dxLogic import Logic


class ResumenDiarioLogic(Logic):
    def __init__(self):
        super().__init__()

    def existenciaRegistro(self, date, idUsuario):
        sqlCount = f"SELECT COUNT(id_registro) from registrodiario where fecha = {date} and id_usuario = {idUsuario};"
        datos = self.database.executeQueryOneRow(sqlCount)
        count = datos.get("COUNT(id_registro)")
        return count

    def imprimeResumenMedidas(self, date, idUsuario):

        count = self.existenciaRegistro(date, idUsuario)

        if count == 1:
            sql = f"select * from registrodiario where id_usuario = {idUsuario} and fecha = {date};"
            resumen = self.database.executeQueryRows(sql)
            return resumen
        else:
            resumen = None
            return resumen

    def porcentajeCalorias(self, date, idUsuario, caloriasRecomendadas):

        sqlSumaCalorias = (
            f"SELECT SUM(calorias*myfitapp.consumoalimento.porcion) as totalCalorias from myfitapp.consumoalimento"
            + f" left outer join myfitapp.producto on myfitapp.consumoalimento.id_producto=myfitapp.producto.id_producto "
            + f"where myfitapp.consumoalimento.id_usuario = {idUsuario} and fecha = {date}"
        )

        datosCalorias = self.database.executeQueryOneRow(sqlSumaCalorias)

        if datosCalorias["totalCalorias"] is None:
            porcentajeCalorias = 0
            return porcentajeCalorias
        elif datosCalorias["totalCalorias"] > caloriasRecomendadas:
            porcentajeCalorias = (
                float(datosCalorias["totalCalorias"]) / caloriasRecomendadas
            ) * 100
            return porcentajeCalorias
        elif datosCalorias["totalCalorias"] == 0:
            porcentajeCalorias = 0
            return porcentajeCalorias
        else:
            porcentajeCalorias = (
                float(datosCalorias["totalCalorias"]) / caloriasRecomendadas
            ) * 100
            return porcentajeCalorias

    def porcentajeGrasasTotales(self, date, idUsuario, grasasRecomendadas):

        sqlSumaGrasasTotales = (
            f"SELECT SUM(grasasTotales*myfitapp.consumoalimento.porcion) as totalGrasas from myfitapp.consumoalimento"
            + f" left outer join myfitapp.producto on myfitapp.consumoalimento.id_producto=myfitapp.producto.id_producto "
            + f"where myfitapp.consumoalimento.id_usuario = {idUsuario} and fecha = {date}"
        )

        datosGrasasTotales = self.database.executeQueryOneRow(sqlSumaGrasasTotales)

        if datosGrasasTotales["totalGrasas"] is None:
            porcentajeGrasasTotales = 0
            return porcentajeGrasasTotales
        elif datosGrasasTotales["totalGrasas"] > grasasRecomendadas:
            porcentajeGrasasTotales = (
                float(datosGrasasTotales["totalGrasas"]) / grasasRecomendadas
            ) * 100
            return porcentajeGrasasTotales
        elif datosGrasasTotales["totalGrasas"] == 0:
            porcentajeGrasasTotales = 0
            return porcentajeGrasasTotales
        else:
            porcentajeGrasasTotales = (
                float(datosGrasasTotales["totalGrasas"]) / grasasRecomendadas
            ) * 100
            return porcentajeGrasasTotales

    def porcentajeColesterol(self, date, idUsuario, colesterolRecomendado):

        sqlSumaColesterol = (
            f"SELECT SUM(colesterol*myfitapp.consumoalimento.porcion) as totalColesterol from myfitapp.consumoalimento"
            + f" left outer join myfitapp.producto on myfitapp.consumoalimento.id_producto=myfitapp.producto.id_producto "
            + f"where myfitapp.consumoalimento.id_usuario = {idUsuario} and fecha = {date}"
        )

        datosColesterol = self.database.executeQueryOneRow(sqlSumaColesterol)

        if datosColesterol["totalColesterol"] is None:
            porcentajeColesterol = 0
            return porcentajeColesterol
        elif datosColesterol["totalColesterol"] > colesterolRecomendado:
            porcentajeColesterol = (
                float(datosColesterol["totalColesterol"]) / colesterolRecomendado
            ) * 100
            return porcentajeColesterol
        elif datosColesterol["totalColesterol"] == 0:
            porcentajeColesterol = 0
            return porcentajeColesterol
        else:
            porcentajeColesterol = (
                float(datosColesterol["totalColesterol"]) / colesterolRecomendado
            ) * 100
            return porcentajeColesterol

    def porcentajeSodio(self, date, idUsuario, sodioRecomendado):

        sqlSumaSodio = (
            f"SELECT SUM(sodio*myfitapp.consumoalimento.porcion) as totalSodio from myfitapp.consumoalimento"
            + f" left outer join myfitapp.producto on myfitapp.consumoalimento.id_producto=myfitapp.producto.id_producto "
            + f"where myfitapp.consumoalimento.id_usuario = {idUsuario} and fecha = {date}"
        )

        datosSodio = self.database.executeQueryOneRow(sqlSumaSodio)

        if datosSodio["totalSodio"] is None:
            porcentajeSodio = 0
            return porcentajeSodio
        elif datosSodio["totalSodio"] > sodioRecomendado:
            porcentajeSodio = (float(datosSodio["totalSodio"]) / sodioRecomendado) * 100
            return porcentajeSodio
        elif datosSodio["totalSodio"] == 0:
            porcentajeSodio = 0
            return porcentajeSodio
        else:
            porcentajeSodio = (float(datosSodio["totalSodio"]) / sodioRecomendado) * 100
            return porcentajeSodio

    def porcentajeAzucares(self, date, idUsuario, azucaresRecomendadas):

        sqlSumaAzucares = (
            f"SELECT SUM(azucares*myfitapp.consumoalimento.porcion) as totalAzucares from myfitapp.consumoalimento"
            + f" left outer join myfitapp.producto on myfitapp.consumoalimento.id_producto=myfitapp.producto.id_producto "
            + f"where myfitapp.consumoalimento.id_usuario = {idUsuario} and fecha = {date}"
        )

        datosAzucares = self.database.executeQueryOneRow(sqlSumaAzucares)

        if datosAzucares["totalAzucares"] is None:
            porcentajeAzucares = 0
            return porcentajeAzucares
        elif datosAzucares["totalAzucares"] > azucaresRecomendadas:
            porcentajeAzucares = (
                float(datosAzucares["totalAzucares"]) / azucaresRecomendadas
            ) * 100
            return porcentajeAzucares
        elif datosAzucares["totalAzucares"] == 0:
            porcentajeAzucares = 0
            return porcentajeAzucares
        else:
            porcentajeAzucares = (
                float(datosAzucares["totalAzucares"]) / azucaresRecomendadas
            ) * 100
            return porcentajeAzucares
