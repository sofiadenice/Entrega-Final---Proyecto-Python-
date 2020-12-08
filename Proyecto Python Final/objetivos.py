from colores import Colores
from prettytable import PrettyTable
from objetivosLogic import ObjetivosLogic


class Objetivos:
    def __init__(self, idUsuario):
        self.colores = Colores()
        self.idUsuario = idUsuario
        self.logic = ObjetivosLogic()
        self.pesoActual = self.logic.getPeso(self.idUsuario)
        self.pesoDeseado = self.logic.getPesoDeseado(self.idUsuario)
        self.altura = self.logic.getAltura(self.idUsuario)
        self.calorias = self.getCalorias()
        self.azucar = self.getAzucar()
        self.grasa = self.getGrasas()
        self.sodio = 1.5
        self.colesterol = 0.45

    def getCalorias(self):
        calorias = 0

        if self.pesoActual > self.pesoDeseado:
            calorias = 22 * (self.pesoDeseado)
        elif self.pesoActual < self.pesoDeseado:
            calorias = 32 * (self.pesoDeseado)
        else:
            calorias = 27 * (self.pesoActual)

        return float(calorias)

    def getAzucar(self):
        azucar = 0
        calAzucar = self.calorias * 0.1
        azucar = calAzucar * 250 / 2000
        return azucar

    def getGrasas(self):
        grasa = 0
        calGrasas = self.calorias * 0.3
        grasa = calGrasas * 200 / 2000
        return grasa

    def nutricion(self):
        print("")
        print("-------------------------------------------------------")
        print(self.colores.blue("Recomendaciones para nutricion"))
        print("-------------------------------------------------------")
        print("")
        print("-------------------------------------------------------")
        print(
            self.colores.red(
                f"Tu límite de calorías diario es de: {self.calorias} kcal"
            )
        )
        print(self.colores.cyan(f"Tu límite de azúcar diario es de: {self.azucar} g"))
        print(self.colores.green(f"Tu límite de grasa diario es de: {self.grasa} g"))
        print(
            self.colores.yellow(
                f"Tu límite de colesterol diario es de: {self.colesterol} g"
            )
        )
        print(self.colores.purple(f"Tu límite de sodio diario es de: {self.sodio} g"))
        print("-------------------------------------------------------")
        print("")

    def ejercicio(self):
        intensidad = self.logic.getIntensidad(self.idUsuario)

        ejercicioDic = self.logic.selectEjercicios(intensidad)

        print("")
        print("-------------------------------------------------------")
        print(self.colores.blue("Recomendaciones de ejercicio"))
        print("-------------------------------------------------------")
        print("")
        table = PrettyTable()
        table.field_names = [
            "Nombre",
            "Parte ejercitada",
            "Repeticiones",
        ]
        for row in ejercicioDic:
            table.add_row([row["nombre"], row["parte"], row["repeticiones"]])
        print(table)
        print("")

    def modificarPeso(self):
        peso = 0.0
        while peso < 10 or peso > 440:
            try:
                peso = float(input("Ingrese su nuevo peso deseado en kilogramos:"))
                if peso < 10 or peso > 440:
                    print(self.colores.red("Ese valor de peso no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red("El campo de peso solo acepta valores numéricos")
                )

        try:
            cambio = self.logic.cambiarPesoDeseado(peso, self.idUsuario)
            if cambio:
                print(
                    self.colores.green(
                        f"Cambio de peso deseado efectuado correctamente"
                    )
                )
            else:
                print(self.colores.red(f"Cambio de intensidad no efectuado"))
        except Exception:
            print(self.colores.red(f"Cambio de intensidad no efectuado"))

    def modificarEjercicio(self):

        while True:
            try:
                print("Ingrese el tipo de intensidad de ejercicio: ")
                print("(1) Principiante")
                print("(2) Intermedio")
                print("(3) Avanzado")
                intensidad = int(input("Ingrese el número de la opción que desea: "))
            except Exception:
                print(self.colores.red("Valor no válido"))

            if intensidad == 1:
                cambio = self.logic.cambiarIntensidad(1, self.idUsuario)
                if cambio:
                    print(
                        self.colores.green(
                            f"Cambio de intensidad efectuado correctamente"
                        )
                    )
                    break
                else:
                    print(self.colores.red(f"Cambio de intensidad no efectuado"))
                    break
            elif intensidad == 2:
                cambio = self.logic.cambiarIntensidad(2, self.idUsuario)
                if cambio:
                    print(
                        self.colores.green(
                            f"Cambio de intensidad efectuado correctamente"
                        )
                    )
                    break
                else:
                    print(self.colores.red(f"Cambio de intensidad no efectuado"))
                    break
            elif intensidad == 3:
                cambio = self.logic.cambiarIntensidad(3, self.idUsuario)
                if cambio:
                    print(
                        self.colores.green(
                            f"Cambio de intensidad efectuado correctamente"
                        )
                    )
                    break
                else:
                    print(self.colores.red(f"Cambio de intensidad no efectuado"))
                    break
            else:
                print(
                    self.colores.red(
                        "Opción no válida. Vuelva a ingresar su respuesta."
                    )
                )
