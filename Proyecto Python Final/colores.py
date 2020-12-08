import os
import sys

os.system("cls")


class Colores:
    def __init__(self):
        self.colors = {
            "black": "\u001b[30;1m",
            "red": "\u001b[31;1m",
            "green": "\u001b[32m",
            "yellow": "\u001b[33;1m",
            "blue": "\u001b[34;1m",
            "magenta": "\u001b[35m",
            "cyan": "\u001b[36m",
            "white": "\u001b[37m",
            "purple": "\u001b[38;5;141m",
            "yellow-background": "\u001b[43m",
            "black-background": "\u001b[40m",
            "cyan-background": "\u001b[46;1m",
        }
        pass

    def colorText(self, text):
        for color in self.colors:
            text = text.replace("[[" + color + "]]", self.colors[color])
        return text

    def red(self, cadena):
        formato = "[[red]]" + cadena + "[[white]]"
        result = self.colorText(formato)
        return result

    def green(self, cadena):
        formato = "[[green]]" + cadena + "[[white]]"
        result = self.colorText(formato)
        return result

    def yellow(self, cadena):
        formato = "[[yellow]]" + cadena + "[[white]]"
        result = self.colorText(formato)
        return result

    def blue(self, cadena):
        formato = "[[blue]]" + cadena + "[[white]]"
        result = self.colorText(formato)
        return result

    def magenta(self, cadena):
        formato = "[[magenta]]" + cadena + "[[white]]"
        result = self.colorText(formato)
        return result

    def cyan(self, cadena):
        formato = "[[cyan]]" + cadena + "[[white]]"
        result = self.colorText(formato)
        return result

    def purple(self, cadena):
        formato = "[[purple]]" + cadena + "[[white]]"
        result = self.colorText(formato)
        return result

    def black(self, cadena):
        formato = "[[black]]" + cadena + "[[white]]"
        result = self.colorText(formato)
        return result

    def white(self, cadena):
        formato = "[[white]]" + cadena + "[[white]]"
        result = self.colorText(formato)
        return result

    def codigosColores(self):

        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                sys.stdout.write("\u001b[38;5;" + code + "m " + code.ljust(4))
            print("\u001b[0m")


# colores = Colores()

# hello = "[[purple]]hello [[blue]]world[[white]]"
# print(colores.colorText(hello))

# codigos = colores.codigosColores()
# Para agregar un color, agreguen este elemento al diccionario self.colors: "{nombreColor}": "\u001b[38;5;{código}m",'
