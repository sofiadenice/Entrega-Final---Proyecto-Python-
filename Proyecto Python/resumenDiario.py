from resumenDiarioLogic import ResumenDiarioLogic
from objetivos import Objetivos
from colores import Colores
from prettytable import PrettyTable
import matplotlib.pyplot as plt


class Resumen:
    def __init__(self, idUsuario):
        self.logic = ResumenDiarioLogic()
        self.objetivos = Objetivos(idUsuario)
        self.colores = Colores()

    def imprimeResumenActual(self, idUsuario):

        date = str("curdate()")
        resumen = self.logic.imprimeResumenMedidas(date, idUsuario)

        print("")
        print("-------------------------------------------------------")
        print(self.colores.blue("Resumen de medidas"))
        print("-------------------------------------------------------")

        if resumen is not None:
            table = PrettyTable()
            table.field_names = [
                "Fecha",
                "Peso",
                "Cintura",
                "Cuello",
            ]
            for row in resumen:
                table.add_row(
                    [
                        row["fecha"],
                        row["pesoActual"],
                        row["cintura"],
                        row["cuello"],
                    ]
                )
            print("")
            print(table)
        else:
            print("")
            print(self.colores.red("No se encontró ningún registro de este día"))

    def imprimeResumenOtroDia(self, idUsuario):
        anno = 0
        while anno < 1000 or anno > 9999:
            try:
                anno = int(input("Ingresa el año deseado (yyyy): "))
                if anno < 1000 or anno > 9999:
                    print(self.colores.red("Ese valor de año no es válido"))
                else:
                    break
            except Exception:
                print(self.colores.red("El campo de año solo acepta valores numéricos"))

        mes = 0
        while mes < 1 or mes > 12:
            try:
                mes = int(input("Ingresa el mes deseado (mm): "))
                if mes < 1 or mes > 12:
                    print(self.colores.red("Ese valor de mes no es válido"))
                else:
                    break
            except Exception:
                print(self.colores.red("El campo de mes solo acepta valores numéricos"))

        while True:
            dia = 0
            while True:
                try:
                    dia = int(input("Ingresa el día deseado (dd): "))
                    break
                except Exception:
                    print(
                        self.colores.red(
                            "El campo de día solo acepta valores numéricos"
                        )
                    )

            if (
                mes == 1
                or mes == 3
                or mes == 5
                or mes == 7
                or mes == 8
                or mes == 10
                or mes == 12
            ):
                if dia < 1 or dia > 31:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia < 1 or dia > 30:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            elif mes == 2 and (
                anno % 4 == 0 and (not (anno % 100 == 0) or anno % 400 == 0)
            ):
                if dia < 1 or dia > 29:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            elif mes == 2:
                if dia < 1 or dia > 28:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            else:
                print(self.colores.red("Ese valor de día no es válido"))

        date = "'" + str(anno) + "-" + str(mes) + "-" + str(dia) + "'"

        resumen = self.logic.imprimeResumenMedidas(date, idUsuario)

        print("")
        print("-------------------------------------------------------")
        print(self.colores.blue("Resumen de medidas"))
        print("-------------------------------------------------------")

        if resumen is not None:
            table = PrettyTable()
            table.field_names = [
                "Fecha",
                "Peso",
                "Cintura",
                "Cuello",
            ]
            for row in resumen:
                table.add_row(
                    [
                        row["fecha"],
                        row["pesoActual"],
                        row["cintura"],
                        row["cuello"],
                    ]
                )
            print("")
            print(table)
        else:
            print("")
            print(
                self.colores.red(
                    "No se encontró ningún registro con la fecha proporcionada"
                )
            )

    def resumenConsumoActual(self, idUsuario):

        date = str("curdate()")
        self.imprimeResumenConsumo(date, idUsuario)

    def resumenConsumoOtrodía(self, idUsuario):

        anno = 0
        while anno < 1000 or anno > 9999:
            try:
                anno = int(input("Ingresa el año deseado (yyyy): "))
                if anno < 1000 or anno > 9999:
                    print(self.colores.red("Ese valor de año no es válido"))
                else:
                    break
            except Exception:
                print(self.colores.red("El campo de año solo acepta valores numéricos"))

        mes = 0
        while mes < 1 or mes > 12:
            try:
                mes = int(input("Ingresa el mes deseado (mm): "))
                if mes < 1 or mes > 12:
                    print(self.colores.red("Ese valor de mes no es válido"))
                else:
                    break
            except Exception:
                print(self.colores.red("El campo de mes solo acepta valores numéricos"))

        while True:
            dia = 0
            while True:
                try:
                    dia = int(input("Ingresa el día deseado (dd): "))
                    break
                except Exception:
                    print(
                        self.colores.red(
                            "El campo de día solo acepta valores numéricos"
                        )
                    )

            if (
                mes == 1
                or mes == 3
                or mes == 5
                or mes == 7
                or mes == 8
                or mes == 10
                or mes == 12
            ):
                if dia < 1 or dia > 31:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia < 1 or dia > 30:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            elif mes == 2 and (
                anno % 4 == 0 and (not (anno % 100 == 0) or anno % 400 == 0)
            ):
                if dia < 1 or dia > 29:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            elif mes == 2:
                if dia < 1 or dia > 28:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            else:
                print(self.colores.red("Ese valor de día no es válido"))

        date = "'" + str(anno) + "-" + str(mes) + "-" + str(dia) + "'"

        self.imprimeResumenConsumo(date, idUsuario)

    def imprimeResumenConsumo(self, date, idUsuario):

        caloriasRecomendadas = self.objetivos.calorias
        grasasRecomendadas = self.objetivos.grasa
        colesterolRecomendado = self.objetivos.colesterol
        sodioRecomendado = self.objetivos.sodio
        azucaresRecomendadas = self.objetivos.azucar

        porcentajeCalorias = self.logic.porcentajeCalorias(
            date, idUsuario, caloriasRecomendadas
        )
        porcentajeGrasasTotales = self.logic.porcentajeGrasasTotales(
            date, idUsuario, grasasRecomendadas
        )
        porcentajeColesterol = self.logic.porcentajeColesterol(
            date, idUsuario, colesterolRecomendado
        )
        porcentajeSodio = self.logic.porcentajeSodio(date, idUsuario, sodioRecomendado)
        porcentajeAzucares = self.logic.porcentajeAzucares(
            date, idUsuario, azucaresRecomendadas
        )

        print("")
        if porcentajeCalorias > 100:
            print(
                self.colores.red(
                    "Has consumido más de las calorias recomendadas. Consumiste "
                    + str(round(porcentajeCalorias - 100, 2))
                    + "% extra"
                )
            )
            porcentajeCalorias = 100
        if porcentajeGrasasTotales > 100:
            print(
                self.colores.red(
                    "Has consumido más de las grasas recomendadas. Consumiste "
                    + str(round(porcentajeGrasasTotales - 100, 2))
                    + "% extra"
                )
            )
            porcentajeGrasasTotales = 100
        if porcentajeColesterol > 100:
            print(
                self.colores.red(
                    "Has consumido más del colesterol recomendado. Consumiste "
                    + str(round(porcentajeColesterol - 100, 2))
                    + "% extra"
                )
            )
            porcentajeColesterol = 100
        if porcentajeSodio > 100:
            print(
                self.colores.red(
                    "Has consumido más del sodio recomendado. Consumiste "
                    + str(round(porcentajeSodio - 100, 2))
                    + "% extra"
                )
            )
            porcentajeSodio = 100
        if porcentajeAzucares > 100:
            print(
                self.colores.red(
                    "Has consumido más de las azúcares recomendadas. Consumiste "
                    + str(round(porcentajeAzucares - 100, 2))
                    + "% extra"
                )
            )
            porcentajeAzucares = 100

        # Gráficos
        label1 = "Consumidas", "Restantes"
        sizes1 = [porcentajeCalorias, 100 - porcentajeCalorias]

        label2 = "Consumidas", "Restantes"
        sizes2 = [porcentajeGrasasTotales, 100 - porcentajeGrasasTotales]

        label3 = "Consumido", "Restante"
        sizes3 = [porcentajeColesterol, 100 - porcentajeColesterol]

        label4 = "Consumido", "Restante"
        sizes4 = [porcentajeSodio, 100 - porcentajeSodio]

        label5 = "Consumidos", "Restantes"
        sizes5 = [porcentajeAzucares, 100 - porcentajeAzucares]

        fig1, axs = plt.subplots(2, 5)
        fig1.suptitle("Consumo del día", fontsize=20)

        axs[0, 0].pie(
            sizes1,
            labels=label1,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 8},
        )
        axs[0, 0].set_title("Calorías")
        axs[0, 0].axis("equal")

        axs[1, 4].pie(
            sizes2,
            labels=label2,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 8},
        )
        axs[1, 4].set_title("Grasas totales")
        axs[1, 4].axis("equal")

        axs[1, 0].pie(
            sizes3,
            labels=label3,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 8},
        )
        axs[1, 0].set_title("Colesterol")
        axs[1, 0].axis("equal")

        axs[1, 2].pie(
            sizes4,
            labels=label4,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 8},
        )
        axs[1, 2].set_title("Sodio")
        axs[1, 2].axis("equal")

        axs[0, 4].pie(
            sizes5,
            labels=label5,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 8},
        )
        axs[0, 4].set_title("Azúcares")
        axs[0, 4].axis("equal")

        axs[0, 2].set_visible(False)
        axs[0, 1].set_visible(False)
        axs[1, 1].set_visible(False)
        axs[0, 3].set_visible(False)
        axs[1, 3].set_visible(False)

        plt.show()
