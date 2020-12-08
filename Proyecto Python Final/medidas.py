from medidasLogic import MedidasLogic
from colores import Colores


class Medidas:
    def __init__(self):
        self.colores = Colores()
        self.logic = MedidasLogic()

    def ingresarPrimerPeso(self, peso, idUsuario):

        self.logic.ingresarPrimerPeso(peso, idUsuario)

    def ingresarPeso(self, idUsuario):
        peso = 0.00
        while peso < 0.01 or peso > 400:
            try:
                peso = float(input("Ingrese su peso en kilogramos: "))
                if peso < 0.01 or peso > 400:
                    print(self.colores.red("Ese valor de peso no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red("El campo de peso solo acepta valores numéricos")
                )

        self.logic.ingresarPeso(peso, idUsuario)

        print("")
        print(self.colores.green("El registro se guardó correctamente"))

    def ingresarCintura(self, idUsuario):
        cintura = 0.00
        while cintura < 0.01 or cintura > 300:
            try:
                cintura = float(input("Ingrese su medida de cintura en centímetros: "))
                if cintura < 0.01 or cintura > 300:
                    print(self.colores.red("Ese valor de cintura no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red(
                        "El campo de cintura solo acepta valores numéricos"
                    )
                )

        self.logic.ingresarCintura(cintura, idUsuario)

        print("")
        print(self.colores.green("El registro se guardó correctamente"))

    def ingresarCuello(self, idUsuario):
        cuello = 0.00
        while cuello < 0.01 or cuello > 200:
            try:
                cuello = float(input("Ingrese su medida de cuello en centímetros: "))
                if cuello < 0.01 or cuello > 200:
                    print(self.colores.red("Ese valor de cuello no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red("El campo de cuello solo acepta valores numéricos")
                )

        self.logic.ingresarCuello(cuello, idUsuario)

        print("")
        print(self.colores.green("El registro se guardó correctamente"))
