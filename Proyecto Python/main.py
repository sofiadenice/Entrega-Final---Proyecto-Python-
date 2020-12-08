from colores import Colores
from menu import Menu
from premium import Premium


idUsuario = 0
colores = Colores()
menu = Menu()

idUsuario = menu.loginMenu()

if idUsuario == 0:
    print("")
    print(colores.green("Finalizando app..."))

else:
    premium = Premium(idUsuario)

    isPremium = premium.getPremium()

    if isPremium:
        menu.menuPremium(idUsuario)
    else:
        menu.menuNoPremium(idUsuario)

    print("")
    print(colores.green("Finalizando app..."))
