from premiumLogic import PremiumLogic
from colores import Colores
import datetime


class Premium:
    def __init__(self, idUser):
        self.idUser = idUser
        self.logic = PremiumLogic()
        self.colores = Colores()
        pass

    def getPremium(self):
        date = datetime.datetime.now()
        premiumDate = self.logic.getPremiumDate(self.idUser)
        if premiumDate > date:
            return True
        else:
            return False

    def addPremium(self, dias):
        date = datetime.datetime.now()
        newDate = date + datetime.timedelta(days=dias)
        anno = newDate.year
        mes = newDate.month
        dia = newDate.day
        cambio = self.logic.changeDate(anno, mes, dia, self.idUser)
        return cambio
