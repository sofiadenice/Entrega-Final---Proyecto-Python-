from dxLogic import Logic


class PremiumLogic(Logic):
    def __init__(self):
        super().__init__()

    def changeDate(self, anno, mes, dia, idUser):

        sqlUpdate = f"UPDATE myfitapp.usuario SET premium = '{anno}-{mes}-{dia}' WHERE id_usuario = {idUser:}"

        result = self.database.executeNonQueryBool(sqlUpdate)

        return result

    def getPremiumDate(self, idUser):

        sqlSelect = f"SELECT * FROM myfitapp.usuario WHERE id_usuario = '{idUser:}'"

        selectUserDic = self.database.executeQueryOneRow(sqlSelect)

        premiumDate = selectUserDic.get("premium")

        return premiumDate