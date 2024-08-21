class Fabrica: # Inicio y creacion de la clase fabrica
    def __init__(self, llantas, color, precio): # Constructor de la clase
        self.llantas = llantas  # Asigna el número de llantas al objeto
        self.color = color  # Asigna el color al objeto
        self.precio = precio  # Asigna el precio al objeto

    def mostrar_datos(self):
        #Muestra los datos del vehículo en la consola.
        print(f"Este vehículo tiene {self.llantas} llantas, es de color {self.color} y cuesta ${self.precio}.")

    def aplicar_descuento(self): # VAriable para aplicar el 10% si la compra > 100.00 
        if self.precio > 100000:
            self.precio *= 0.9  # Aplica el descuento del 10%
            print("Se ha aplicado un descuento del 10% al precio.")

class Auto(Fabrica):# Clase para representar un automóvil
    def __init__(self, llantas, color, precio, marca):
        super().__init__(llantas, color, precio)  # Llama al constructor de la clase padre
        self.marca = marca  # Asigna la marca del automóvil

class Moto(Fabrica):  # Clase para representar una motocicleta
    def __init__(self, llantas, color, precio, cilindrada):
        super().__init__(llantas, color, precio)  # Llama al constructor de la clase padre
        self.cilindrada = cilindrada  # Asigna la cilindrada del motor

# Creación de objetos
mi_auto = Auto(4, "rojo", 20000, "Toyota")
mi_moto = Moto(2, "negro", 120000, 600)

# Mostrar datos iniciales
mi_auto.mostrar_datos()
mi_moto.mostrar_datos()

# Aplicar descuento a la moto y mostrar los datos actualizados
mi_moto.aplicar_descuento()
mi_moto.mostrar_datos()