from login import Login
from signUp import SignUp
from resumenDiario import Resumen
from medidas import Medidas
from objetivos import Objetivos
from alimentacion import Alimentacion
from ejercicio import Ejercicio
from evolucion import Evolucion
from colores import Colores
from premium import Premium


class Menu:
    def __init__(self):
        self.idUser = 0
        eleccion = 0
        idUsuario = 0
        self.colores = Colores()
        pass

    def loginMenu(self):
        while True:
            print("")
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print(self.colores.blue("APLICACIÓN FIT"))
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print(
                self.colores.magenta(
                    '"Cuida tu cuerpo. Es el único lugar que tienes para vivir."'
                )
            )
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print("(1) Iniciar sesión")
            print("(2) Crear una cuenta")
            print("(0) Salir")
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print("")
            while True:
                try:
                    eleccion = int(input("Ingrese el número de la opción que desea: "))
                    break
                except Exception:
                    print(self.colores.red("Este campo solo acepta valores numéricos"))
            print("")

            if eleccion == 0:
                return 0
                break
            elif eleccion == 1:
                login = Login()
                usuario = input("Ingrese su nombre de usuario: ")
                contra = input("Ingrese su contraseña: ")
                comprobacion = login.comprobacion(usuario, contra)
                if comprobacion:
                    print("")
                    print(self.colores.green("Iniciando sesión..."))
                    self.idUsuario = login.idUsuario()
                    return self.idUsuario
                    break
                else:
                    print("")
                    print(self.colores.red("Usuario o contraseña incorrectos"))
            elif eleccion == 2:
                signUp = SignUp()
                while True:
                    usuario = input("Ingrese un nombre de usuario: ")
                    compUsuario = signUp.comprobacionUsuario(usuario)
                    if compUsuario:
                        while True:
                            correo = input("Ingrese su correo electronico: ")
                            compCorreo = signUp.comprobacionCorreo(correo)
                            if compCorreo:
                                while True:
                                    contra = input(
                                        "Ingrese una contraseña de mínimo 4 y máximo 12 caracteres: "
                                    )
                                    compContra = signUp.comprobacionContra(contra)
                                    if compContra:
                                        signUp.guardaDatos()
                                        break
                                    else:
                                        print(self.colores.red("Contraseña no válida"))
                                break
                            else:
                                print(
                                    self.colores.red(
                                        "Ya existe una cuenta vinculada a ese correo electrónico"
                                    )
                                )
                        break
                    else:
                        print(self.colores.red("El usuario que ha ingresado ya existe"))
            else:
                print(self.colores.red("La opción que ingresó no es válida"))

    def menuNoPremium(self, idUsuario):
        premium = Premium(idUsuario)
        while not premium.getPremium():

            if idUsuario == 0:
                break

            print("")
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print(self.colores.blue("MENÚ PRINCIPAL"))
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print("(1) Mostrar resumen diario")
            print("(2) Ingresar medidas")
            print("(3) Objetivos")
            print("(4) Registrar alimento")
            print("(5) Registrar ejercicio")
            print("(6) Hazte premium")
            print("(0) Salir")
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print("")
            while True:
                try:
                    eleccion = int(input("Ingrese el número de la opción que desea: "))
                    break
                except Exception:
                    print(self.colores.red("Este campo solo acepta valores numéricos"))
            print("")

            if eleccion == 0:
                break
            elif eleccion == 1:
                resumen = Resumen(idUsuario)
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE RESUMEN DIARIO"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Resumen de medidas de hoy")
                    print("(2) Resumen de medidas de otro día")
                    print("(3) Resumen del consumo de hoy")
                    print("(4) Resumen del consumo de otro día")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        resumen.imprimeResumenActual(idUsuario)
                    elif opcion == 2:
                        resumen.imprimeResumenOtroDia(idUsuario)
                    elif opcion == 3:
                        resumen.resumenConsumoActual(idUsuario)
                    elif opcion == 4:
                        resumen.resumenConsumoOtrodía(idUsuario)
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 2:
                medidas = Medidas()
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE INGRESO DE MEDIDAS"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Ingresar peso del día")
                    print("(2) Ingresar registro de cintura")
                    print("(3) Ingresar registro de cuello")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        medidas.ingresarPeso(idUsuario)
                    elif opcion == 2:
                        medidas.ingresarCintura(idUsuario)
                    elif opcion == 3:
                        medidas.ingresarCuello(idUsuario)
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 3:
                objetivos = Objetivos(idUsuario)
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE OBJETIVOS"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Nutrición recomendada")
                    print("(2) Ejercicio recomendado")
                    print("(3) Modificar objetivos de peso")
                    print("(4) Modificar objetivos de ejercicio")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        objetivos.nutricion()
                    elif opcion == 2:
                        objetivos.ejercicio()
                    elif opcion == 3:
                        objetivos.modificarPeso()
                    elif opcion == 4:
                        objetivos.modificarEjercicio()
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 4:
                alimentacion = Alimentacion(idUsuario)
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE REGISTROS DE ALIMENTOS"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Agregar alimento")
                    print("(2) Buscar alimento")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print("")
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                            print("")
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        alimento = alimentacion.agregarAlimento()

                        if alimento:
                            print("")
                            print(
                                self.colores.green("Alimento registrado correctamente")
                            )
                        else:
                            alimentacion.buscarAlimento()

                    elif opcion == 2:
                        alimentacion.buscarAlimento()
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 5:
                ejercicio = Ejercicio(idUsuario)
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE REGISTROS DE EJERCICIOS"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Registrar ejercicio de cardio")
                    print("(2) Buscar ejercicio de cardio")
                    print("(3) Registrar ejercicio de peso")
                    print("(4) Buscar ejercicio de peso")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:

                        ejer = ejercicio.agregarCardio()

                        if ejer:
                            print("")
                            print(
                                self.colores.green("Ejercicio registrado correctamente")
                            )
                        else:
                            ejercicio.buscarCardio()

                    elif opcion == 2:
                        ejercicio.buscarCardio()

                    elif opcion == 3:

                        ejer = ejercicio.agregarPeso()

                        if ejer:
                            print("")
                            print(
                                self.colores.green("Ejercicio registrado correctamente")
                            )
                        else:
                            ejercicio.buscarPeso()

                    elif opcion == 4:
                        ejercicio.buscarPeso()
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 6:
                while True:
                    print("")
                    print(
                        self.colores.purple(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.magenta("HAZTE PREMIUM"))
                    print(
                        self.colores.purple(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.yellow("Beneficios:"))
                    print(self.colores.cyan("Creación de recetas personalizadas"))
                    print(
                        self.colores.cyan(
                            "Creación de ejercicios cardiovasculares personalizados"
                        )
                    )
                    print(
                        self.colores.cyan(
                            "Creación de ejercicios de peso personalizados"
                        )
                    )
                    print(self.colores.cyan("Evolución de tu progreso"))
                    print(
                        self.colores.purple(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    print("")
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("Planes se subscripción"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Plan de 1 mes     $ 1.99")
                    print("(2) Plan de 3 meses   $ 3.99")
                    print("(3) Plan de 1 año     $ 9.99")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        result = premium.addPremium(30)
                        if result:
                            print(
                                "Subscripción realizada correctamente. Vuelva a iniciar sesión para acceder a las funciones Premium."
                            )
                            break
                        else:
                            print("No se pudo realizar la subscripción")
                    elif opcion == 2:
                        result = premium.addPremium(90)
                        if result:
                            print(
                                "Subscripción realizada correctamente. Vuelva a iniciar sesión para acceder a las funciones Premium."
                            )
                            break
                        else:
                            print("No se pudo realizar la subscripción")
                    elif opcion == 3:
                        result = premium.addPremium(365)
                        if result:
                            print(
                                "Subscripción realizada correctamente. Vuelva a iniciar sesión para acceder a las funciones Premium."
                            )
                            break
                        else:
                            print("No se pudo realizar la subscripción")
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            else:
                print(self.colores.red("La opción que ingresó no es válida"))

    def menuPremium(self, idUsuario):
        while True:

            if idUsuario == 0:
                break

            print("")
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print(self.colores.blue("MENÚ PRINCIPAL"))
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print("(1) Mostrar resumen diario")
            print("(2) Ingresar medidas")
            print("(3) Objetivos")
            print("(4) Registrar alimento")
            print("(5) Registrar ejercicio")
            print("(6) Evolución de mi progreso")
            print("(0) Salir")
            print(
                self.colores.cyan(
                    "-------------------------------------------------------"
                )
            )
            print("")
            while True:
                try:
                    eleccion = int(input("Ingrese el número de la opción que desea: "))
                    break
                except Exception:
                    print(self.colores.red("Este campo solo acepta valores numéricos"))
            print("")

            if eleccion == 0:
                break
            elif eleccion == 1:
                resumen = Resumen(idUsuario)
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE RESUMEN DIARIO"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Resumen de medidas de hoy")
                    print("(2) Resumen de medidas de otro día")
                    print("(3) Resumen del consumo de hoy")
                    print("(4) Resumen del consumo de otro día")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        resumen.imprimeResumenActual(idUsuario)
                    elif opcion == 2:
                        resumen.imprimeResumenOtroDia(idUsuario)
                    elif opcion == 3:
                        resumen.resumenConsumoActual(idUsuario)
                    elif opcion == 4:
                        resumen.resumenConsumoOtrodía(idUsuario)
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 2:
                medidas = Medidas()
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE INGRESO DE MEDIDAS"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Ingresar peso del día")
                    print("(2) Ingresar registro de cintura")
                    print("(3) Ingresar registro de cuello")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        medidas.ingresarPeso(idUsuario)
                    elif opcion == 2:
                        medidas.ingresarCintura(idUsuario)
                    elif opcion == 3:
                        medidas.ingresarCuello(idUsuario)
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 3:
                objetivos = Objetivos(idUsuario)
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE OBJETIVOS"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Nutrición recomendada")
                    print("(2) Ejercicio recomendado")
                    print("(3) Modificar objetivos de peso")
                    print("(4) Modificar objetivos de ejercicio")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        objetivos.nutricion()
                    elif opcion == 2:
                        objetivos.ejercicio()
                    elif opcion == 3:
                        objetivos.modificarPeso()
                    elif opcion == 4:
                        objetivos.modificarEjercicio()
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 4:
                alimentacion = Alimentacion(idUsuario)
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE REGISTROS DE ALIMENTOS"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Agregar alimento")
                    print("(2) Buscar alimento")
                    print("(3) Crear receta")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print("")
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                            print("")
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        alimento = alimentacion.agregarAlimento()

                        if alimento:
                            print("")
                            print(
                                self.colores.green("Alimento registrado correctamente")
                            )
                        else:
                            alimentacion.buscarAlimento()

                    elif opcion == 2:
                        alimentacion.buscarAlimento()
                    elif opcion == 3:
                        alimentacion.crearReceta()
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 5:
                ejercicio = Ejercicio(idUsuario)
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE REGISTROS DE EJERCICIOS"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Registrar ejercicio de cardio")
                    print("(2) Buscar ejercicio de cardio")
                    print("(3) Crear un nuevo ejercicio de cardio")
                    print("(4) Registrar ejercicio de peso")
                    print("(5) Buscar ejercicio de peso")
                    print("(6) Crear un nuevo ejercicio de peso")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:

                        ejer = ejercicio.agregarCardio()

                        if ejer:
                            print("")
                            print(
                                self.colores.green("Ejercicio registrado correctamente")
                            )
                        else:
                            ejercicio.buscarCardio()

                    elif opcion == 2:
                        ejercicio.buscarCardio()

                    elif opcion == 3:
                        ejercicio.crearCardio()

                    elif opcion == 4:

                        ejer = ejercicio.agregarPeso()

                        if ejer:
                            print("")
                            print(
                                self.colores.green("Ejercicio registrado correctamente")
                            )
                        else:
                            ejercicio.buscarPeso()

                    elif opcion == 5:
                        ejercicio.buscarPeso()
                    elif opcion == 6:
                        ejercicio.crearPeso()
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            elif eleccion == 6:
                evolucion = Evolucion()
                while True:
                    print("")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print(self.colores.blue("MENÚ DE EVOLUCIÓN DE PROGRESO"))
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("(1) Evolución de mi peso")
                    print("(2) Evolución de cintura")
                    print("(3) Evolución de cuello")
                    print("(4) Calorías consumidas")
                    print("(5) Calorías quemadas")
                    print("(6) Evolución de ejercicios de peso")
                    print("(0) Regresar al menú principal")
                    print(
                        self.colores.cyan(
                            "-------------------------------------------------------"
                        )
                    )
                    print("")
                    while True:
                        try:
                            opcion = int(
                                input("Ingrese el número de la opción que desea: ")
                            )
                            break
                        except Exception:
                            print(
                                self.colores.red(
                                    "Este campo solo acepta valores numéricos"
                                )
                            )
                    print("")
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        evolucion.evoPeso(idUsuario)
                    elif opcion == 2:
                        evolucion.evoCintura(idUsuario)
                    elif opcion == 3:
                        evolucion.evoCuello(idUsuario)
                    elif opcion == 4:
                        evolucion.evoCalConsumidas(idUsuario)
                    elif opcion == 5:
                        evolucion.evoCalQuemadas(idUsuario)
                    elif opcion == 6:
                        evolucion.evoEjPeso(idUsuario)
                    elif opcion == 7:
                        evolucion.evoTiempo(idUsuario)
                    else:
                        print(self.colores.red("La opción que ingresó no es válida"))
            else:
                print(self.colores.red("La opción que ingresó no es válida"))
