# from databaseX import DatabaseX
from prettytable import PrettyTable
from colores import Colores
from alimentacionLogic import AlimentacionLogic


class Alimentacion:
    def __init__(self, idUser):
        self.idUser = idUser
        self.colores = Colores()
        self.idAlimento = 0
        self.logic = AlimentacionLogic()

    def agregarAlimento(self):

        while True:

            while True:
                try:
                    idAlimento = int(
                        input(
                            "Ingrese el ID de su alimento, si desconoce el ID ingrese 0 para ir al buscador: "
                        )
                    )

                    if idAlimento < 0 or idAlimento is None:
                        print("")
                        print(colores.red("Ese valor de id Alimento no es válido"))
                        print("")
                    else:
                        self.idAlimento = idAlimento
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de id Alimento solo acepta valores numéricos"
                        )
                    )
                    print("")

            if idAlimento == 0:
                result = False
                break

            else:

                rowsNum = self.logic.getBuscarDos(idAlimento, self.idUser)

                if rowsNum == 1:
                    result = True
                    break
                else:
                    print("")
                    print(
                        self.colores.red(
                            "El ID que ingresó no existe, por favor ingrese un ID válido"
                        )
                    )
                    print("")

        if result:

            while True:
                try:
                    porcion = int(
                        input(
                            "Ingrese la cantidad de porciones del alimento que consumió: "
                        )
                    )
                    if porcion <= 0 or porcion is None:
                        print("")
                        print(self.colores.red("Ese valor de porcion no es válido"))
                        print("")
                    else:

                        # meter a la BD
                        self.logic.getAgregar(self.idAlimento, self.idUser, porcion)

                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de porcion solo acepta valores numéricos"
                        )
                    )
                    print("")

            return result

        else:
            return result

    def buscarAlimento(self):

        print("")
        # variables a ungresar

        alimento = str(
            input(
                "Ingrese el alimento que quiere buscar o presione Enter para ver todos: "
            )
        )

        # meter a la BD

        alimento1 = self.logic.getBuscar(self.idUser, alimento)

        print("")
        print("-------------------------------------------------------")
        print(self.colores.blue("Alimentos"))
        print("-------------------------------------------------------")

        # imprimir info con prettytable

        table = PrettyTable()
        table.field_names = [
            "ID",
            "Nombre",
            "Gramos por porción",
            "Calorías",
            "Grasas totales",
            "Colesterol",
            "Sodio",
            "Azúcares",
        ]
        for row in alimento1:
            table.add_row(
                [
                    row["id_producto"],
                    row["nombre"],
                    row["porcion"],
                    row["calorias"],
                    row["grasasTotales"],
                    row["colesterol"],
                    row["sodio"],
                    row["azucares"],
                ]
            )
        print(table)
        print("")

    def crearReceta(self):
        print("")
        # variables a ingresar
        while True:
            try:
                nombre = str(input("Ingrese el nombre del nuevo alimento: "))
                if nombre == "":
                    print("")
                    print(self.colores.red("Ese valor de nombre no es válido"))
                    print("")
                elif len(nombre) > 20:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de nombre no puede tener más de 20 caracteres"
                        )
                    )
                    print("")
                else:
                    break

            except Exception:
                print("")
                print(self.colores.red("El campo de nombre solo acepta texto"))
                print("")

        # nombre = str(input("Ingrese el nombre del nuevo alimento: "))
        while True:
            try:
                porciones = float(
                    input("Ingrese la cantidad de gramos por porción de su alimento: ")
                )
                if porciones < 0.0 or porciones is None:
                    print("")
                    print(self.colores.red("Ese valor de porciones no es válido"))
                    print("")
                else:

                    break

            except Exception:
                print("")
                print(
                    self.colores.red(
                        "El campo de porciones solo acepta valores numericos"
                    )
                )
                print("")
        # porciones = float(
        #    input("Ingrese la cantidad de gramos por porción de su alimento: "))
        while True:
            try:
                calorias = float(
                    input("Ingrese la cantidad de la calorias en kilocalorias: ")
                )
                if calorias < 0.0 or calorias is None:
                    print("")
                    print(self.colores.red("Ese valor de calorias no es válido"))
                    print("")
                else:
                    break

            except Exception:
                print("")
                print(
                    self.colores.red(
                        "El campo de calorias solo acepta valores numericos"
                    )
                )
                print("")
        # calorias = float(input("Ingrese la cantidad de la caloria: "))
        while True:
            try:
                grasaTotales = float(
                    input("Ingrese la cantidad de grasas totales en gramos: ")
                )
                if grasaTotales < 0.0 or grasaTotales is None:
                    print("")
                    print(self.colores.red("Ese valor de grasa Totales no es válido"))
                    print("")
                else:

                    break

            except Exception:
                print("")
                print(
                    self.colores.red(
                        "El campo de grasas totales solo acepta valores numericos"
                    )
                )
                print("")
        # grasaTotales = float(input("Ingrese la cantidad de grasas totales: "))
        while True:
            try:
                colesterol = float(
                    input("Ingrese la cantidad de colesterol en gramos: ")
                )
                if colesterol < 0.0 or colesterol is None:
                    print("")
                    print(self.colores.red("Ese valor de colesterol no es válido"))
                    print("")
                else:

                    break

            except Exception:
                print("")
                print(
                    self.colores.red(
                        "El campo de cantidad de colesteron solo acepta valores numericos"
                    )
                )
                print("")
        # colesterol = float(input("Ingrese la cantidad de colesterol: "))
        while True:
            try:
                sodio = float(input("Ingrese la cantidad de sodio en gramos: "))
                if sodio < 0.0 or sodio is None:
                    print("")
                    print(self.colores.red("Ese valor de sodio no es válido"))
                    print("")
                else:

                    break

            except Exception:
                print("")
                print(
                    self.colores.red("El campo de sodio solo acepta valores numericos")
                )
                print("")
        # sodio = float(input("Ingrese la cantidad de sodio: "))
        while True:
            try:
                azucares = float(input("Ingrese la cantidad de azúcares en gramos: "))
                if azucares < 0.0 or azucares is None:
                    print("")
                    print(self.colores.red("Ese valor de azucares no es válido"))
                    print("")
                else:

                    break

            except Exception:
                print("")
                print(
                    self.colores.red(
                        "El campo de azucares solo acepta valores numericos"
                    )
                )
                print("")
        # azucares = float(input("Ingrese la cantidad de azucares: "))
        print("")
        # ingresas a la BD
        self.logic.crearReceta(
            nombre,
            porciones,
            calorias,
            grasaTotales,
            colesterol,
            sodio,
            azucares,
            self.idUser,
        )
