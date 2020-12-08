from prettytable import PrettyTable
from colores import Colores
from ejecicioLogic import EjercicioLogic


class Ejercicio:
    def __init__(self, idUser):
        self.idUser = idUser
        self.colores = Colores()
        self.idEjercicio = 0
        self.ejercicioLogic = EjercicioLogic()

    def agregarCardio(self):

        while True:

            while True:
                try:
                    idEjercicio = int(
                        input(
                            "Ingrese el ID de su ejercicio, si desconoce el ID ingrese 0 para ir al buscador: "
                        )
                    )

                    if idEjercicio < 0 or idEjercicio is None:
                        print("")
                        print(colores.red("Ese valor de ID de ejercicio no es válido"))
                        print("")
                    else:
                        self.idEjercicio = idEjercicio
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de ID de ejercicio solo acepta valores numéricos"
                        )
                    )
                    print("")

            if idEjercicio == 0:
                result = False
                break

            else:
                rowsNum = self.ejercicioLogic.buscardos(self.idUser, idEjercicio)

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
                    tiempo = int(
                        input(
                            "Ingrese la cantidad de tiempo que se ejercitó en minutos: "
                        )
                    )
                    if tiempo <= 0 or tiempo is None:
                        print("")
                        print(self.colores.red("Ese valor de tiempo no es válido"))
                        print("")

                    else:

                        # meter a la BD
                        self.ejercicioLogic.agregarCardio(
                            self.idUser, idEjercicio, tiempo
                        )
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de tiempo solo acepta valores numéricos enteros"
                        )
                    )
                    print("")

            return result

        else:
            return result

    def buscarCardio(self):
        print("")

        # variables a ingresar

        EjercicioCardio = str(
            input(
                "Ingrese el ejercicio de cardio que quiere buscar o presione Enter para ver todos: "
            )
        )
        print("")

        # meter a la BD

        ejercicio1 = self.ejercicioLogic.buscarCardio(EjercicioCardio, self.idUser)

        # imprimir info con prettytable

        print("")
        print("-------------------------------------------------------")
        print(self.colores.blue("Ejercicios de cardio"))
        print("-------------------------------------------------------")

        table = PrettyTable()
        table.field_names = [
            "id_ejercicio",
            "nombre Ejercicio",
            "calorias quemadas por minuto",
        ]
        for row in ejercicio1:
            table.add_row(
                [
                    row["id_ejercicio"],
                    row["nombreEjercicio"],
                    row["caloriasQuemadas"],
                ]
            )
        print(table)
        print("")

    def crearCardio(self):
        print("")

        # variables a ingresar

        while True:
            try:
                nombre = str(input("Ingrese el nombre del nuevo ejercicio: "))
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

        while True:
            try:
                caloriasQuemadas = float(
                    input("Ingrese la cantidad de calorias quemadas por minuto: ")
                )

                if caloriasQuemadas < 0.0 or caloriasQuemadas is None:
                    print("")
                    print(self.colores.red("Ese valor de porciones no es válido"))
                    print("")
                else:

                    break

            except Exception:
                print("")
                print(
                    self.colores.red(
                        "El campo de calorias quemadas solo acepta valores numericos"
                    )
                )
                print("")

        # ingresar a la BD

        self.ejercicioLogic.crearCardio(nombre, caloriasQuemadas, self.idUser)

    def agregarPeso(self):

        while True:

            while True:
                try:
                    idEjercicio = int(
                        input(
                            "Ingrese el ID de su ejercicio, si desconoce el ID ingrese 0 para ir al buscador: "
                        )
                    )

                    if idEjercicio < 0 or idEjercicio is None:
                        print("")
                        print(colores.red("Ese valor de ID de ejercicio no es válido"))
                        print("")
                    else:
                        self.idEjercicio = idEjercicio
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de ID de ejercicio solo acepta valores numéricos"
                        )
                    )
                    print("")

            if idEjercicio == 0:
                result = False
                break

            else:

                rowsNum = self.ejercicioLogic.getBuscarFuerzaDos(
                    self.idEjercicio, self.idUser
                )

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
                    repeticiones = int(
                        input("Ingrese la cantidad de repeticiones realizadas: ")
                    )

                    if repeticiones <= 0 or repeticiones is None:
                        print("")
                        print(
                            self.colores.red("Ese valor de repeticiones no es válido")
                        )
                        print("")
                    else:
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de repeticiones solo acepta valores numéricos"
                        )
                    )
                    print("")

            while True:
                try:
                    series = int(input("Ingrese la cantidad de series realizadas: "))
                    if series < 0 or series is None:
                        print("")
                        print(self.colores.red("Ese valor de series no es válido"))
                        print("")
                    else:
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de series solo acepta valores numericos"
                        )
                    )
                    print("")

            while True:
                try:
                    peso = int(
                        input(
                            "Ingrese la cantidad de libras aplicadas en su ejercicio: "
                        )
                    )
                    if peso < 0 or peso is None:
                        print("")
                        print(self.colores.red("Ese valor de peso no es válido"))
                        print("")
                    else:
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de peso solo acepta valores numericos"
                        )
                    )
                    print("")

            # meter a la BD

            self.ejercicioLogic.getFuerza(
                self.idUser, self.idEjercicio, repeticiones, series, peso
            )

            return result

        else:
            return result

    def buscarPeso(self):
        print("")

        # variables a ingresar
        EjercicioPeso = str(
            input(
                "Ingrese el ejercicio de peso que quiere buscar o presione Enter para ver todos: "
            )
        )
        print("")

        # meter a la BD
        ejercicio1 = self.ejercicioLogic.getBuscarFuerza(self.idUser, EjercicioPeso)

        # imprimir info con prettytable

        print("")
        print("-------------------------------------------------------")
        print(self.colores.blue("Ejercicios de fuerza"))
        print("-------------------------------------------------------")

        table = PrettyTable()
        table.field_names = [
            "id_ejercicio",
            "nombreEjercicio",
            "parteDelCuerpo",
        ]
        for row in ejercicio1:
            table.add_row(
                [
                    row["id_ejercicio"],
                    row["nombreEjercicio"],
                    row["parteDelCuerpo"],
                ]
            )
        print(table)
        print("")

    def crearPeso(self):
        print("")

        # variables a ingresar
        while True:
            try:
                nombre = str(input("Ingrese el nombre del nuevo ejercicio: "))
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

        while True:
            try:
                parteDelCuerpo = str(
                    input("Ingrese la parte del cuerpo que ejercita: ")
                )
                if parteDelCuerpo == "":
                    print("")
                    print(
                        self.colores.red("Ese valor de partes del cuerpo no es válido")
                    )
                    print("")
                elif len(parteDelCuerpo) > 20:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de parte del cuerpo no puede tener más de 20 caracteres"
                        )
                    )
                    print("")
                else:
                    break

            except Exception:
                print("")
                print(
                    self.colores.red("El campo de parte del cuerpo solo acepta texto")
                )
                print("")

        print("")

        self.ejercicioLogic.getCrearFuerza(nombre, parteDelCuerpo, self.idUser)
