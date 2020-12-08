from evolucionLogic import EvolucionLogic
import matplotlib.pyplot as plt
from colores import Colores
from prettytable import PrettyTable


class Evolucion:
    def __init__(self):
        self.logic = EvolucionLogic()
        self.colores = Colores()
        self.listaDato = []
        self.listaFecha = []

    def evoPeso(self, idUsuario):

        datos = self.logic.evoPeso(idUsuario)

        if datos is not None:
            for row in datos:
                if row["pesoActual"] > 0:
                    fechaFixed = str(row["fecha"])
                    self.listaFecha.append(fechaFixed[:10])
                    self.listaDato.append(float(row["pesoActual"]))
            Ejey = self.listaDato
            Ejex = self.listaFecha
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(Ejex, Ejey, marker="o", color="#7581bf")
            ax.set(
                title="Evolución de peso diario", xlabel="Fecha", ylabel="Peso\n(kg)"
            )
            plt.xticks(rotation=45)
            plt.grid(True, color="#b4b5bf")
            plt.show()
        self.listaDato = []
        self.listaFecha = []

    def evoCintura(self, idUsuario):

        datos = self.logic.evoCintura(idUsuario)

        if datos is not None:
            for row in datos:
                if row["cintura"] > 0:
                    fechaFixed = str(row["fecha"])
                    self.listaFecha.append(fechaFixed[:10])
                    self.listaDato.append(float(row["cintura"]))
            Ejey = self.listaDato
            Ejex = self.listaFecha
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(Ejex, Ejey, marker="o", color="#7581bf")
            ax.set(title="Evolución de cintura", xlabel="Fecha", ylabel="Medida\n(cm)")
            plt.xticks(rotation=45)
            plt.grid(True, color="#b4b5bf")
            plt.show()
        self.listaDato = []
        self.listaFecha = []

    def evoCuello(self, idUsuario):

        datos = self.logic.evoCuello(idUsuario)

        if datos is not None:
            for row in datos:
                if row["cuello"] > 0:
                    fechaFixed = str(row["fecha"])
                    self.listaFecha.append(fechaFixed[:10])
                    self.listaDato.append(float(row["cuello"]))
            Ejey = self.listaDato
            Ejex = self.listaFecha
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(Ejex, Ejey, marker="o", color="#7581bf")
            ax.set(title="Evolución de Cuello", xlabel="Fecha", ylabel="Medida\n(cm)")
            plt.xticks(rotation=45)
            plt.grid(True, color="#b4b5bf")
            plt.show()
        self.listaDato = []
        self.listaFecha = []

    def evoCalConsumidas(self, idUsuario):

        datos = self.logic.evoCalConsumidas(idUsuario)

        if datos is not None:
            for row in datos:
                if row["caloriasTotales"] > 0:
                    fechaFixed = str(row["fecha"])
                    self.listaFecha.append(fechaFixed[:10])
                    self.listaDato.append(float(row["caloriasTotales"]))
            Ejey = self.listaDato
            Ejex = self.listaFecha
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(Ejex, Ejey, marker="o", color="#7581bf")
            ax.set(
                title="Evolución de calorias consumidas",
                xlabel="Fecha",
                ylabel="Calorias\n(kcal)",
            )
            plt.xticks(rotation=45)
            plt.grid(True, color="#b4b5bf")
            plt.show()
        self.listaDato = []
        self.listaFecha = []

    def evoCalQuemadas(self, idUsuario):

        datos = self.logic.evoCalQuemadas(idUsuario)

        if datos is not None:
            for row in datos:
                if row["quemadasTotales"] > 0:
                    fechaFixed = str(row["fecha"])
                    self.listaFecha.append(fechaFixed[:10])
                    self.listaDato.append(float(row["quemadasTotales"]))
            Ejey = self.listaDato
            Ejex = self.listaFecha
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(Ejex, Ejey, marker="o", color="#7581bf")
            ax.set(
                title="Evolución de calorias quemadas",
                xlabel="Fecha",
                ylabel="Calorias\n(kcal)",
            )
            plt.xticks(rotation=45)
            plt.grid(True, color="#b4b5bf")
            plt.show()
        self.listaDato = []
        self.listaFecha = []

    def evoEjPeso(self, idUsuario):

        datos = self.logic.evoEjPeso(idUsuario)

        print("")
        print("-------------------------------------------------------")
        print(self.colores.blue("Evolución de ejercicios de peso"))
        print("-------------------------------------------------------")

        if datos is not None:
            table = PrettyTable()
            table.field_names = [
                "Fecha",
                "Ejercicio",
                "Parte del cuerpo",
                "Repeticiones",
                "Series",
                "Peso Aplicado",
            ]
            for row in datos:
                table.add_row(
                    [
                        row["fecha"],
                        row["nombreEjercicio"],
                        row["parteDelCuerpo"],
                        row["repeticiones"],
                        row["series"],
                        row["pesoAplicado"],
                    ]
                )
            print("")
            print(table)
