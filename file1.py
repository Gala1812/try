import time

class Taximetro():
    def __init__(self):
        self.tiempo = 0
        self.distancia = 0
        self.precio = 0
        self.tarifa = 0.5
        self.tarifa_tiempo = 0.1
        self.tarifa_distancia = 0.2

    def iniciar_viaje(self):
        self.tiempo = time.time()

    def finalizar_viaje(self):
        tiempo_final = time.time()
        self.tiempo = tiempo_final - self.tiempo
        self.distancia = 10
        self.precio = self.distancia * self.tarifa_distancia + self.tiempo * self.tarifa_tiempo
        return self.precio